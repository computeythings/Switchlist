from ipaddress import IPv4Network
from WebApp.WebServer.Job import Job
from WebApp.WebServer.Device import Device
import WebApp.WebServer.Backend as Backend
import asyncio, logging, traceback, os, json, time, sys
from aiohttp import web
from aiohttp_sse import sse_response
from aiohttp_cors import setup, ResourceOptions
logger = logging.getLogger(__name__)

if getattr(sys, 'frozen', False):
    bundle_dir = application_path = sys._MEIPASS
elif __file__:
    bundle_dir = os.path.dirname(__file__)

class Server:
    def __init__(self, database=None, connect_method=None):
        self.connect = connect_method
        self.app = web.Application()
        self.pubqueue = asyncio.Queue()
        self.database = database
        self.discover_queue = asyncio.Queue()
        self.discovering = None
        self.scrape_queue = asyncio.Queue()
        self.web_queues = {}
        self.scraping = None
        self.last_event_id = -1
        self.eventHistory = {}
        self.distributor_active = False
        self.serviced = []

        async def iostream(request):
            '''
            Server-side Event publishing URL
            '''
            last_event_client = request.rel_url.query['event-id']
            async with sse_response(request) as response:
                sse_queue_id = time.time()
                sse_queue = await self.provision_web_client(sse_queue_id)
                if last_event_client:
                    logger.info(f'Client connected with {self.last_event_id - last_event_client} missing events.')
                    while last_event_client < self.last_event_id:
                        logger.debug(f'Re-publishing event: {last_event_client}')
                        await response.send(f'{json.dumps(self.eventHistory[last_event_client])}')
                        last_event_client+= 1
                while True:
                    data = await sse_queue.get()
                    logger.debug(f'Publishing event: {self.last_event_id}')
                    try:
                        await response.send(f'{json.dumps(data)}')
                    except:
                        break
                    sse_queue.task_done()
                await self.deprovision_web_client(sse_queue_id)
            return response
        self.app.router.add_get('/iostream', iostream)
        
        async def devices_get(request):
            ''' 
            Returns a list of all network devices in database
            '''
            return web.json_response(
                self.database.get_devices(), 
                status=201
            )
        self.app.router.add_get('/api/v1/devices', devices_get)

        async def devices_post(request):
            '''
            Adds/Deletes/Modifies(?) a network device within the SQL database
            Most likely just used to blacklist IPs from scans.
            '''
            req = await request.json()
            ip_list = [json.dumps(i) for i in req['ipList']]
            if (req['method'] == 'DELETE'):
                logger.info(f'Removing devices: {ip_list}')
                delete_results = self.database.remove_devices(ip_list)
                logging.debug(f'Delete results:\n{delete_results}')
                return web.json_response(
                    {'message': f'Removed device: {ip_list}'}, 
                    status = 201
                )
        self.app.router.add_post('/api/v1/devices', devices_post)

        async def sites_get(request):
            '''
            Returns a list of sites:
            [
                {
                    id: 1,
                    name: 'SITE1', 
                    subnets: ['192.168.0.0/24', '192.168.1.1/24']
                },
                ...
            ]
            '''
            return web.json_response(
                self.database.get_sites(),
                status=201
            )
        self.app.router.add_get('/api/v1/sites', sites_get)

        async def sites_post(request):
            '''
            Updates sites from list of sites received in POST
            
            POST form:
            {
                sites: [
                    {
                        name: 'SITE1', 
                        subnets: ['192.168.0.0/24', '192.168.1.0/24']
                    },
                    {
                        name: 'SITE2', 
                        subnets: ['192.168.10.0/24', '192.168.11.0/24']
                    },
                ]
            }
            '''
            req = await request.json()
            updated_sites = self.database.set_sites(req['sites'])
            await self.sse_queue({'type': 'site_update', 'sites': updated_sites})
            return web.json_response(
                {'message': 'Sites Updating'}, 
                status = 201
            )
        self.app.router.add_post('/api/v1/sites', sites_post)

        async def discover_get(request):
            '''
            Returns the status of the current discover job including:
                Status: Scanning/Idle
                Start time/date
                Subnets: List of subnets to scan
                Percent complete of each subnet: (Completed/Total) * 100 %
                Duration: Total runtime
                Devices found: new devices found from scan
            '''
            if self.discovering is None:
                return web.json_response('No Active Job'), 201
            return web.json_response(
                self.discovering.web_dump(), 
                status = 201
            )
        self.app.router.add_get('/api/v1/discover', discover_get)

        async def discover_post(request):
            '''
            Pings a list of subnets provided as 'subnets'
            Should asynchronously discover devices and periodically publish updates.
            If the 'scrape' variable is true, devices should be scraped if found online
            POST form:
            {
                addresses: ['XXX.XXX.XXX.XXX',...],
                scrape: True/False
            }
            '''
            try:
                req = await request.json()
                if len(req['addresses']) > 0:
                    ips = [IPv4Network(subnet) for subnet in req['addresses']]
                # If an empty array is supplied, scan all subnets in sites
                else:
                    ips = []
                    for site in self.database.get_sites():
                        ips+= [IPv4Network(subnet) for subnet in site['subnets']]
                if len(ips) <= 0:
                    # Nothing to discover
                    return web.Response(status = 204)
                if req['scrape']:
                    username = req['username']
                    password = req['password']
                    job_data = {
                        'user': os.getlogin(),
                        'type': 'scrape',
                        'target': ips,
                        'data': {
                            'user': username,
                            'password': password
                        }
                    }
                else:
                    job_data = {
                        'user': os.getlogin(),
                        'type': 'discover',
                        'target': ips
                    }
                discover_job = Job(database=self.database, publisher=self.sse_queue, **job_data)
                asyncio.create_task(self.queue_discover(discover_job))
                return web.json_response(
                    discover_job.web_dump(), 
                    status = 201
                )
            except:
                logger.error(traceback.print_exc())
                return web.json_response(
                    {'message': 'Malformed request'}, 
                    status=400
                )
        self.app.router.add_post('/api/v1/discover', discover_post)

        async def scrape_get(request):
            '''
            Returns the status of the current scrape job including:
                Status: Scraping/Idle
                Start time/date
                All devices: List of all IPs to scrape
                Devices completed: List of completed IPs
                Percent complete: (Completed/Total) * 100 %
                Duration: Total runtime
                User: username of user scanning
            '''
            if self.scraping is None:
                return web.json_response(
                    {'message': 'No Active Job'}, 
                    status = 201
                )
            return web.json_response(
                self.scraping.web_dump(), 
                status = 201
            )
        self.app.router.add_get('/api/v1/scrape', scrape_get)

        async def scrape_post(request):
            '''
            Scrapes a list provided as 'addresses' using the provided username and password.
            Should asynchronously scrape devices and periodically return updates:
            POST form:
            {
                ips: ['XXX.XXX.XXX.XXX',...],
                username: 'user',
                password: 'secret'
            }
            '''
            try:
                req = await request.json()
                if len(req['addresses']) > 0:
                    ips = [IPv4Network(ip) for ip in req['addresses']]
                # If an empty array is supplied, scan all subnets in sites
                else:
                    ips = []
                    for row in self.database.get_devices():
                        ips+= [IPv4Network(device['scan_ip']) for device in row]
                username = req['username']
                password = req['password']
                job_data = {
                    'user': os.getlogin(),
                    'type': 'scrape',
                    'target': ips,
                    'data': {
                        'username': username,
                        'password': password
                    }
                }
                scrape_job = Job(database=self.database, publisher=self.sse_queue, **job_data)
                asyncio.create_task(self.queue_scrape(scrape_job))
                return web.json_response(
                    {'message': 'Scrape Job Started.'}, 
                    status = 201
                )
            except:
                logger.error(traceback.print_exc())
                return web.json_response(
                    {'message': 'Malformed request'}, 
                    status = 400
                )
        self.app.router.add_post('/api/v1/scrape', scrape_post)

        async def jobs_get(request):
            ''' 
            Gets job history
            '''
            return web.json_response(
                self.database.get_jobs(),
                status = 201
            )
        self.app.router.add_get('/api/v1/jobs', jobs_get)

        async def index(request):
            '''
            Render application
            '''
            return web.FileResponse(
                os.path.join(bundle_dir,'templates','index.html'),
                status=201
            )
        self.app.router.add_get('/', index)
        self.app.router.add_static('/static', os.path.join(bundle_dir,'static'))

        async def update_securecrt(request):
            '''
            Update local workstation's SecureCRT sessions
            '''
            update_list = await request.json()
            switches = self.database.get_devices()

            # Create a 1:1 map of subnets and their respective site names
            sites = {}
            for site in self.database.get_sites():
                sites[site['name']] = []
                for subnet in site['subnets']:
                    sites[site['name']]+= [str(i) for i in IPv4Network(subnet).hosts()]
            # Update switches to include site name
            for switch in switches:
                site_name = 'Other'
                for site in sites:
                    if switch['scan_ip'] in sites[site]:
                        site_name = site
                        break
                switch.update({'site': site_name})
            # Update SecureCRT with current switch list
            logger.info('POST: crtupdate')
            Backend.update_localhost(switches)
            return web.json_response(
                    {'message': 'Update sent'}, 
                    status = 201
                )
        self.app.router.add_post('/api/v1/crtupdate', update_securecrt)

    '''
        Provisions an async queue for a web client that will receive all updates
    '''
    async def provision_web_client(self, client_id):
        client_queue = asyncio.Queue()
        self.web_queues[client_id] = (client_queue)
        logger.info(f'Added web client. {len(self.web_queues.keys())} clients total.')
        return client_queue
    
    '''
        Deprovisions a queue from a dead client
    '''
    async def deprovision_web_client(self, client_id):
        logger.info(f'Removing client {client_id}')
        del self.web_queues[client_id]
        logger.debug(f'{len(self.web_queues.keys())} clients remaining.')

    '''
        Queues a job to check reachability of a list of IPs
    '''
    async def queue_discover(self, job):
        await self.discover_queue.put(job)
        if self.discovering is None:
            await self.start_discovery()
    '''
        Starts a new discovery worker that pulls from queue until all jobs are complete.
    '''
    async def start_discovery(self):
        while self.discover_queue.qsize() > 0:
            job: Job = await self.discover_queue.get() # pull job from queue
            self.discovering = job
            await job.start() # Update info and write to database
            for subnet in job.target:
                for ipv4addr in subnet.hosts():
                    ip = str(ipv4addr)
                    device_online = await self.discover(ip) # wait for ping result
                    await job.update(ip) # Update ip as completed
                    self.database.set_reachability(Device(scan_ip=ip, reachable=device_online).sql_dump())
                    # send update out to web clients
                    await self.sse_queue({'type': 'device_update', 'ip': ip, 'attributes': {'reachable': device_online}, 'scanning': False})
            await job.complete() # Update info and write to database
            self.discover_queue.task_done() # mark task complete
        self.discovering = None
    '''
        A simple ping test to see if a device is online
        @param(ipv4addr):
            may be input as an ipaddress.IPv4Address object - convert to string before procecssing
    '''
    async def discover(self, ip):
        ping = await asyncio.create_subprocess_exec(
            'ping','-n','1','-w','5', ip,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await ping.communicate()
        if ping.returncode == 0:
            return True
        else:
            return False

    '''
        Queues a job to scrape info from a list of IPs
    '''
    async def queue_scrape(self, job):
        await self.scrape_queue.put(job)
        if self.scraping is None:
            await self.start_scraping()
    '''
        Asynchronously scrape info from devices in each job until the queue is empty:
        job = {
            'id': round(time.time()*1000),
            'user': 'windows_user',
            'type': 'scrape',
            'target': ips,
            'start_time': 0,
            'duration': 0,
            'status': 'queued',
            'data': {
                'username': 'ssh_user',
                'password': 'secret'
            }
        }
    '''
    async def start_scraping(self):
        while self.scrape_queue.qsize() > 0:
            job: Job = await self.scrape_queue.get() # pull job from queue
            self.scraping = job
            await job.start() # Update info and write to database
            for subnet in job.target:
                for ipv4addr in subnet.hosts():
                    ip = str(ipv4addr)
                    await self.sse_queue({'type': 'device_update', 'ip': ip, 'attributes': {}, 'scanning': True})
                    device_info = await self.scrape(ip, job.data['username'], job.data['password']) # await device info
                    await job.update(ip) # Update ip as completed
                    self.database.update_device(Device(**device_info).sql_dump())
                    # send update out to web clients
                    await self.sse_queue({'type': 'device_update', 'id': job.id, 'ip': ip, 'attributes': device_info, 'scanning': False})
            await job.complete() # Update info and write to database
            self.scrape_queue.task_done()
        self.scraping = None
    '''
        SSH into device @param(ip) and collect information
    '''
    async def scrape(self, ip, username, password):
        if not await self.discover(ip):
            return { 'scan_ip': ip, 'reachable': False, 'updated': time.time() }
        try:
            switch = self.connect(username, password, ip)
            if switch.make == 'Cisco':
                switch.readinfo()
                switch.parse_domain()
                switch.parse_interfaces()
                switch.parse_upstream()
                switch.parse_cdp()
                switch.parse_fips()
                switch.parse_user_ports()
                switch.save_offline()
            else:
                switch.readinfo()
                switch.parse_all()
            switch_info = switch.json_web()
            switch_info['updated'] = time.time()
        except:
            logger.error(f'Unable to log into {ip}')
            logger.debug(traceback.print_exc(), 'map_host')
            switch_info = { 'scan_ip': ip, 'managed': False, 'reachable': True, 'updated': time.time() }
        finally:
            try:
                if switch and switch.connected():
                    switch.disconnect()
            except:
                pass
        logger.info('Finished scrape for ' + ip)
        return switch_info

    '''
        Queues a server-side event
    '''
    async def sse_queue(self, event):
        await self.pubqueue.put(event)
        if not self.distributor_active:
            asyncio.create_task(self.sse_distribute())

    '''
        Redistributes server-side events to all web clients
    '''
    async def sse_distribute(self):
        while self.pubqueue.qsize() > 0:
            self.distributor_active = True
            event = await self.pubqueue.get()
            self.last_event_id+= 1
            event['eventId'] = self.last_event_id

            for queue_id in self.web_queues:
                await self.web_queues[queue_id].put(event)
                
            self.eventHistory[self.last_event_id] = event
            # Keep a maximum size of 500 for event history
            if len(self.eventHistory) > 500:
                del self.eventHistory[self.last_event_id - 500]
            self.pubqueue.task_done()
        self.distributor_active = False

        

    '''
        Start web server
    '''
    def run(self, host='0.0.0.0', port=5000):
        print('Starting server...')
        cors = setup(self.app, defaults={
            "*": ResourceOptions(
                    allow_credentials=True,
                    expose_headers="*",
                    allow_headers="*"
                )
            })
        for route in list(self.app.router.routes()):
            cors.add(route)
        web.run_app(self.app, host=host, port=port)