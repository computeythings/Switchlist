class Device:
    def __init__(self, **kwargs):
        self.scan_ip = ''
        self.base_subnet = ''
        self.hostname = ''
        self.ip_addresses = {}
        self.make = ''
        self.model = []
        self.base_model = ''
        self.firmware = ''
        self.serial = []
        self.upstream = ''
        self.fips = False
        self.neighbors = {}
        self.updated = 0
        self.uptime = 0
        self.users = 0
        self.base_mac = []
        self.managed = False
        self.reachable = False
        for key, value in kwargs.items():
            if key == 'target' and isinstance(value, str):
                value = value.split(',') # split values stored as SQL string
            setattr(self, key, value)

    async def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self.sql_dump()

    def sql_dump(self):
        return {
            'scan_ip': self.scan_ip,
            'base_subnet': self.base_subnet,
            'hostname': self.hostname,
            'ip_addresses': self.ip_addresses,
            'make': self.make,
            'model': self.model,
            'base_model': self.base_model,
            'firmware': self.firmware,
            'serial': self.serial,
            'upstream': self.upstream,
            'fips': self.fips,
            'neighbors': self.neighbors,
            'updated': self.updated,
            'uptime': self.uptime,
            'users': self.users,
            'base_mac': self.base_mac,
            'managed': self.managed,
            'reachable': self.reachable
        }