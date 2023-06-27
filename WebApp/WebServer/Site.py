from ipaddress import IPv4Network

class Site:
    def __init__(self, **kwargs):
        self.name = kwargs['name'],
        if 'subnets' in kwargs:
            for subnet in kwargs['subnets']:
                self.subnets.append(IPv4Network(subnet))

    '''
        Validates IP networks and updates current subnets
    '''
    def set_subnets(self, subnets):
        new_subnets = []
        for subnet_string in subnets:
            subnet = IPv4Network(subnet_string)
            new_subnets.append(subnet)
        self.subnets = new_subnets

    '''
        Returns serialized data including all IPs of each subnet from network address to broadcast address
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
    def dump(self):
        all_ips = {}
        for subnet in self.subnets:
            all_ips[str(subnet)] = []
            for ip in subnet:
                all_ips[str(subnet)].append(str(ip))
        return {
            'name': self.name,
            'subnets': all_ips
        }