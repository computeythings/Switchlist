import sqlite3, json, logging
logger = logging.getLogger(__name__)

class NetworkDeviceDatabase:
    def __init__(self, db=':memory:'):
        self.db = db
        self.connect()
        self.cur.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table';
        """)
        tables = self.cur.fetchall()
        if not {'name': 'devices'} in tables:
            logger.info('Creating table devices.')
            self.cur.execute("""
                CREATE TABLE devices(
                    scan_ip UNIQUE PRIMARY KEY NOT NULL, 
                    base_subnet, 
                    hostname, 
                    ip_addresses, 
                    make, 
                    model, 
                    base_model, 
                    firmware, 
                    serial, 
                    upstream, 
                    fips, 
                    neighbors, 
                    updated, 
                    uptime, 
                    users, 
                    base_mac, 
                    managed,
                    reachable
                );"""
            )
            self.con.commit()
        if not {'name': 'sites'} in tables:
            logger.info('Creating table sites.')
            self.cur.execute("""
                CREATE TABLE 
                    sites(
                        name UNIQUE PRIMARY KEY,
                        subnets
                    );
                """
            )
            self.con.commit()
        if not {'name': 'jobs'} in tables:
            logger.info('Creating table jobs.')
            self.cur.execute("""
                CREATE TABLE 
                    jobs(
                        id INTEGER UNIQUE PRIMARY KEY,
                        user,
                        type,
                        target,
                        size INTEGER,
				        start_time INTEGER,
                        duration INTEGER,
                        status
                    );
                """
            )
            self.con.commit()

    def dict_format(self, cursor, row):
        dict_formatted = {}
        for idx, col in enumerate(cursor.description):
            column_name = col[0]
            row_value = row[idx]
            if isinstance(row_value, str):
                try:
                    dict_formatted[column_name] = json.loads(row_value)
                    continue
                except:
                    pass
            dict_formatted[column_name] = row_value
        return dict_formatted

    def query(self, query, args={}, query_raw=False):
        if args != {}:
            sql_args = {}
            if query_raw:
                sql_args = args
            else:
                for key, value in args.items():
                    sql_args[key] = json.dumps(value)
            res = self.cur.execute(query, sql_args)
        else:
            res = self.cur.execute(query)
        list_results = res.fetchall()
        if 'UPDATE' in query or 'INSERT' in query or 'DELETE' in query or 'REPLACE' in query:
            logger.debug(f'Modified {res.rowcount} devices')
            try:
                logger.debug(f'Committing query: {query}')
                self.con.commit()
            except:
                logger.error(f'Failed to commit transcation: $({query})')
        else:
            logger.debug(f'Found {len(list_results)} devices')
        return list_results

    def get_devices(self):
        query_string = """
            SELECT * FROM devices WHERE true;
        """
        return self.query(query_string)

    def add_device(self, device):
        # Named key insertion to sanitize input
        query_string = """
            INSERT INTO devices VALUES(
                :scan_ip, 
                :base_subnet, 
                :hostname, 
                :ip_addresses, 
                :make, 
                :model, 
                :base_model, 
                :firmware, 
                :serial, 
                :upstream, 
                :fips, 
                :neighbors, 
                :updated, 
                :uptime, 
                :users, 
                :base_mac, 
                :managed,
                :reachable
            );
        """
        return self.query(query_string, device)

    def update_device(self, attrs):
        query_string = """
            UPDATE devices
            SET
            base_subnet = :base_subnet, 
            hostname = :hostname, 
            ip_addresses = :ip_addresses, 
            make = :make, 
            model = :model, 
            base_model = :base_model, 
            firmware = :firmware, 
            serial = :serial, 
            upstream = :upstream, 
            fips = :fips, 
            neighbors = :neighbors, 
            updated = :updated, 
            uptime = :uptime, 
            users = :users, 
            base_mac = :base_mac, 
            managed = :managed,
            reachable = :reachable
            WHERE scan_ip == :scan_ip;
        """
        return self.query(query_string, attrs)
    
    def remove_devices(self, ip_list):
        '''
        Remove the devices matching ips listed in @param(ip_list)
        '''
        substitution_string = ','.join('?'*len(ip_list))
        query_string = f"""
            DELETE FROM devices WHERE scan_ip IN ({substitution_string});
        """
        return self.query(query_string, ip_list, query_raw=True)
    
    '''
        INSERT or UPDATE
    '''
    def set_reachability(self, attrs):
        try:
            return self.add_device(attrs)
        except:
            query_string = """
                UPDATE devices 
                SET reachable = :reachable
                WHERE scan_ip == :scan_ip;
            """
            return self.query(query_string, attrs)

    '''
        Updates site information to match list of given names a subnet lists:
        @param(sites):
        [
            {'name': 'site1', 'subnets': ['192.168.0.0/24','192.168.1.0/24']},
            {'name': 'site2', 'subnets': ['192.168.2.0/24']},
        ]

        Stores values in database as a dictionary alongside cooresponding subnet contents:
        [
            {
                'name': 'site1',
                'subnets': {
                    '192.168.0.0/24': ['192.168.0.0','192.168.0.1',...,'192.168.0.255'],
                    '192.168.1.0/24': ['192.168.1.0','192.168.1.1',...,'192.168.1.255']
                }
            }
        ]
    '''
    def set_sites(self, sites): 
        query_string = """
            REPLACE INTO sites
                (name, subnets)
                VALUES
                (:name, :subnets);
        """
        for site in sites:
            self.query(query_string, site)

        # clean up leftover sites
        sites_final = self.get_sites()
        remove_sites = []
        for site in sites_final:
            if not site in sites:
                # JSON dumps key value to match self.qeury() input
                remove_sites.append(json.dumps(site['name'])) 
        if len(remove_sites) > 0:
            substitution_string = ','.join('?'*len(remove_sites))
            query_string = f'DELETE FROM sites WHERE name IN ({substitution_string});'
            self.query(query_string, remove_sites, query_raw=True)
            return self.get_sites()

        return sites_final

    '''
        Removes the site matching name @param(site_name)
    '''
    def remove_site(self, site_name):
        query_string = """
            DELETE FROM sites WHERE name == ?;
        """
        self.query(query_string, site_name)

    '''
        Returns all sites in database in a web-friendly format:
        {
            'name': 'EXAMPLE-SUBNET',
            'subnets': {
                '192.168.0.0/24': [
                    '192.168.0.0','192.168.0.1',...,'192.168.0.255'
                ],
                '192.168.1.0/25': [
                    '192.168.1.0','192.168.1.1',...,'192.168.0.127'
                ]
            }
        }
    '''
    def get_sites(self):
        query_string = """
            SELECT * FROM sites WHERE true;
        """
        return self.query(query_string)

    def add_job(self, job):
        query_string = """
            INSERT INTO jobs VALUES (
                :id,
                :user,
                :type,
                :target,
                :size,
				:start_time,
                :duration,
                :status
            );
        """
        self.query(query_string, job)
        
    '''
        Appends @param(ip_processed) to the task_completed column of job matching @param(id)
        and updates the duration of the job
    '''
    def update_job(self, job):
        query_string = """
            UPDATE jobs 
            SET status = :status,
                duration = :duration,
                start_time = :start_time
            WHERE id = :id;
        """
        self.query(query_string, job)
    
    def get_jobs(self):
        query_string = 'SELECT * FROM jobs;'
        return self.query(query_string)

    def connect(self):
        self.con = sqlite3.connect(self.db)
        self.con.row_factory = self.dict_format
        self.cur = self.con.cursor()

    def close(self):
        self.con.close()
    
    def __del__(self):
        self.close()