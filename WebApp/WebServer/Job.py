import time
from WebApp.WebServer.NetworkDeviceDatabase import NetworkDeviceDatabase

class Job:
    def __init__(self, database=None, publisher=None, **kwargs):
        self.database = database
        self.id = round(time.time()*1000)
        self.publish = publisher
        self.user = 'system'
        self.type = 'blank'
        self.target = []
        self.completed = []
        self.start_time = 0
        self.duration = 0
        self.size = 0
        self.status = 'queued'
        self.data = {} # variable for extra data such as SSH credentials
        for key, value in kwargs.items():
            if key == 'target' and isinstance(value, str):
                value = value.split(',') # split values stored as SQL string
            setattr(self, key, value)
        for subnet in self.target:
            # Add subnet to job size (minus to for network/broadcast addresses)
            self.size+= len(list(subnet.hosts()))

        database.add_job(self.sql_dump())
    
    async def start(self):
        self.start_time = time.time()
        self.status = 'processing'
        self.database.update_job(self.sql_dump())

    async def update(self, completed, update_database=False):
        self.duration = time.time() - self.start_time
        self.completed.append(completed)
        # don't update database - too costly for most updates
        await self.update_connections(update_database)

    async def complete(self):
        self.duration = time.time() - self.start_time
        self.status = 'completed'
        await self.update_connections()

    async def cancel(self):
        self.duration = time.time() - self.start_time
        self.status = 'cancelled'
        await self.update_connections()
            
    async def update_connections(self, update_database=True):
        # update web clients
        if not self.publish is None:
            await self.publish({'type': 'job_update', 'job': self.web_dump()})
        # update database
        if update_database:
            self.database.update_job(self.sql_dump())

    def sql_dump(self):
        return {
            'id': self.id,
            'user': self.user,
            'type': self.type,
            'target': ','.join([str(subnet) for subnet in self.target]),
            'size': self.size,
            'start_time': round(self.start_time * 1000),
            'duration': round(self.duration * 1000),
            'status': self.status
        }
    def web_dump(self):
        return {
            'id': self.id,
            'user': self.user,
            'type': self.type,
            'target': ','.join([str(subnet) for subnet in self.target]),
            'completed': self.completed,
            'size': self.size,
            'start_time': round(self.start_time * 1000),
            'duration': round(self.duration * 1000),
            'status': self.status
        }