'''
    This class allows a user to connect to a device over a serial COM port to send commands

    Author:
    SrA Gonnella, 13 DEC 2022
'''
from netmiko import ConnectHandler
from .Cisco import Cisco

def connect(**kwargs):
    serial_port = kwargs.get('COM', None)
    if not serial_port:
        raise ValueError('Invalid COM port')
    username = kwargs.get('username',None)
    password = kwargs.get('password',None)
    secret = kwargs.get('enable',None)
    device = {
        'device_type': 'cisco_ios_serial',
        'serial_settings': f'COM{serial_port}', 
        'conn_type':'Serial'
    }
    if username:
        device['username'] = username
    if password:
        device['password'] = password
    if secret:
        device['secret'] = secret

    connection = ConnectHandler(**device)
    connection.enable()
    prompt = connection.find_prompt()
    device['hostname'] = prompt[:-1]
    return Cisco(conn=connection, **device)

