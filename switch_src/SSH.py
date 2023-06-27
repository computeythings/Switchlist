'''
    The proper implementation of the Switch.py module - i.e. handled within
    Python entirely, does not rely on SecureCRT.

    This module requires the installation of the netmiko package.
    This is likely going to be run as part of a pre-packaged .exe file
    to prevent burdening NIPR users with the install of PIP packages 
    (PyPI is not trusted on NIPR and cannot be easily used from the CLI.)

    SrA Gonnella, Bryan
    7 NOV 2022
'''
import subprocess, getpass, logging

from netmiko import SSHDetect, ConnectHandler, NetmikoAuthenticationException
from .Cisco import Cisco
from .Brocade import Brocade
logger = logging.getLogger(__name__)

prompts = ['#','>']

'''
	Get device login information from CLI input
'''
def info_prompt():
	username = input('SSH Username: ')
	if username == '':
		raise Exception('no username, no login.')
	password = getpass.getpass('SSH Password: ')
	if password == '':
		raise Exception('Blank passwords are a STIG violation.\nSECURITY BREACH.\nPROCESS SELF-DESTRUCTING')
	return username.strip(), password.strip()

# This will ping the device before attempting to connect to save time waiting for SSH timeouts
def host_online(ip):
    try:
        output = subprocess.check_output("ping -n 1 -w 2 %s" % ip, shell=True, universal_newlines=True)
        if 'unreachable' in output:
            logger.info(f'%s: {ip} offline', 'host_online')
            return False
        else:
            return True
    except Exception as e:
            logger.info(f'%s: {ip} offline', 'host_online')
            return False
    

def ssh_connect(username, password, host, device_type=''):
    device = {
        'device_type': 'autodetect',
        'ip': host,
        'username': username,
        'password': password,
        'port': '22'
    }
    if device_type == '':
        device_type = SSHDetect(**device).autodetect()
        if device_type is None:
            device_type = 'brocade_fastiron'
        device['device_type'] = device_type
        logger.debug(f'%s: Found device type: {device_type}', 'connect')
    else:
        if 'hT' in device_type:
            logger.debug(f'%s: {host} cached as Brocade device', 'connect')
            device['device_type'] = 'brocade_fastiron'
        elif 'NX-OS' in device_type:
            logger.debug(f'%s: {host} cached as Nexus device', 'connect')
            device['device_type'] = 'cisco_nxos'
        else:
            logger.debug(f'%s: {host} cached as Cisco device', 'connect')
            device['device_type'] = 'cisco_ios'
    return ConnectHandler(**device)

# Returns a switch Object based on the prompt recieved on successful SSH login
def init(connection, host):
    prompt = connection.find_prompt()
    hostname = prompt[:-1]
    logger.debug(f'%s: Grabbed prompt {prompt}', 'init')
    device = {
        'ip': host, 
        'hostname':hostname, 
        'conn':connection, 
        'conn_type':'SSH'
    }
    if 'brocade' in connection.device_type:
        logger.debug('%s: Found Brocade switch', 'init')
        return Brocade(**device)
    if 'cisco' in connection.device_type:
        logger.debug('%s: Found Cisco switch', 'init')
        if prompt[-1] == '>':
            logger.warning(f'%s: Cisco switch {host} in non-privileged mode.', 'init')
            device['privileged'] = False
        return Cisco(**device)
    logger.error(f'%s: Unhandled device type: {connection.device_type}', 'init')
    return None
        
# Callable function for use by external modules
def connect(username, password, host, brand='', ignore_ping=False):
    logger.info(f'%s: Connecting to device {host}', 'connect')
    if ignore_ping:
        logger.debug(f'%s: Ignoring device online check.', 'connect')
    if ignore_ping or host_online(host):
        try:
            connection = ssh_connect(username, password, host, brand)
        except NetmikoAuthenticationException:
            logger.error(f'%s: Bad login credentials for {host}', 'connect')
            return None
        return init(connection, host)
    logger.warning(f'%s: Host {host} offline', 'connect')
    return None