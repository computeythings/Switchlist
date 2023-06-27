# $language = "python"
# $interface = "1.0"

##
#    25 MAR 2021
#    Script to import existing switch list as SecureCRT Sessions
#    Author: A1C Gonnella, Bryan
#    Misawa AB
##

import shutil
import getpass
import json
import os, sys
import SecureCRT

DEBUG = False

darkthemepath = 'cisco_dark.ini' 
lightthemepath = 'cisco_light.ini'

def copy_themes(current_dir):
    '''
    Copy themes into local user's secureCRT keyword directory
    '''
    shutil.copyfile(current_dir + '\\' + darkthemepath, 'C:\Users\%s\AppData\Roaming\VanDyke\Config\Keywords\%s' %(getpass.getuser(),darkthemepath))
    shutil.copyfile(current_dir + '\\' + lightthemepath, 'C:\Users\%s\AppData\Roaming\VanDyke\Config\Keywords\%s' %(getpass.getuser(),lightthemepath))

def jsonimport(filepath):
    if not os.path.exists(filepath):
        filepath = crt.Dialog.FileOpenDialog('Open Switch List JSON file', 'Open', 'switches.json')
    with open(filepath,'r') as file:
        switches = json.load(file)
    return switches
    
def config(objConfig, theme):
    '''
    Setup default configuration settings
    '''
    if theme == 'light':
        config_light(objConfig)
    if theme == 'dark':
        config_dark(objConfig)
    objConfig.SetOption('Protocol Name', 'SSH2') # always use ssh2
    objConfig.SetOption('Emulation','Xterm') 
    objConfig.SetOption('ANSI Color', True)
    objConfig.SetOption('Color Scheme Overrides Ansi Color', True)
    objConfig.SetOption('Highlight Color', True)
    objConfig.SetOption('Highlight Reverse Video', False)
    objConfig.SetOption('Auth Prompts in Window', True)
    objConfig.SetOption('Key Exchange Algorithms','curve25519-sha256,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group18-sha512,diffie-hellman-group16-sha512,diffie-hellman-group14-sha256,diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,gss-group1-sha1-toWM5Slw5Ew8Mqkay+al2g==,gss-gex-sha1-toWM5Slw5Ew8Mqkay+al2g==,diffie-hellman-group1-sha1')
    
def config_dark(objConfig):
    objConfig.SetOption('Color Scheme', 'Espresso')
    objConfig.SetOption('Keyword Set', 'cisco_dark')

def config_light(objConfig):
    objConfig.SetOption('Color Scheme', 'Novel')
    objConfig.SetOption('Keyword Set', 'cisco_light')

def list_to_config(jsonlist, default_theme, l3_theme):
    '''
    Converts a list of JSON objects to SecureCRT session objects.
    @param jsonlist: {
        "sites": [{
            id: 1,
            name: 'SITE1', 
            subnets: ['192.168.0.0/24', '192.168.1.1/24'],
            ...
        }...]
        "switches": [{
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
        },...]
    }
    '''
    username = crt.Dialog.Prompt('Enter username to save to profile')
    for device in jsonlist:
        if device['reachable'] != True:
            continue
        hostname = device['hostname'] or 'UNKNOWN'
        switchip = device['scan_ip']
        crt.Session.SetStatusText('Updating information for switch ' + switchip + ' - ' + hostname)
        objConfig = crt.OpenSessionConfiguration('Default')
        objConfig.SetOption('Hostname',switchip) # hostname = switch ip address (CRT decided this format, it's stupid),
        if username != '':
            objConfig.SetOption('Username', username)
        layer3_types = ['Switch-RTR','Router','Nexus']
        if device['model'] in layer3_types:
            config(objConfig, l3_theme)
        else:
            config(objConfig, default_theme)
        objConfig.Save(device['site'] + '/' + switchip + ' - ' + hostname) # save default as session with current name

def get_theme_prefs():
    '''
    Get user preference for SecureCRT themes. Option to have separate theme for layer 3 devices
    If preference is none, current themes will not be modified.
    '''
    default_theme = 'none'
    l3_theme = 'none'
    try:
        theme = crt.Dialog.Prompt(
            """\n
            0: Dark \n
            1: Light \n
            2: Light w/ Layer-3 devices Dark \n
            3: Dark w/ Layer-3 devices Light \n
            4: None
            """, 
            "Pick a theme (Enter the number):"
        )
        if theme == "4":
            pass
        if theme == "3":
            default_theme = 'dark'
            l3_theme = 'light'
        if theme == "2":
            default_theme = 'light'
            l3_theme = 'dark'
        if theme == "1" or 'light' in theme.lower(): # take into account people not reading
            default_theme = 'light'
            l3_theme = 'light'
        if theme == "0" or 'dark' in theme.lower():# take into account people not reading
            default_theme = 'dark'
            l3_theme = 'dark'
    except:
        crt.Dialog.MessageBox('Bad theme entered. No themes for you.')
    
    return default_theme, l3_theme
    
def main():
    '''
    Main method to be run from CLI as SecureCRT script.
    e.g.: PS#> SecureCRT.exe /SCRIPT session_import.py /ARG "C:/path/to/switchlist.json"
    '''
    # Confirm proper arguments supplied
    list_path = sys.argv[-1]
    if not list_path.endswith(".json"):
        return crt.Dialog.MessageBox("Unable to locate JSON data", "ERROR", ICON_WARN)
    jsonlist = jsonimport(list_path)
    current_dir = os.path.dirname(os.path.realpath(__file__))

    copy_themes(current_dir)
    default_theme, l3_theme = get_theme_prefs()

    list_to_config(jsonlist, default_theme, l3_theme)
    
    # update default options
    defaultConfig = crt.OpenSessionConfiguration('Default')
    config(defaultConfig, default_theme)
    defaultConfig.Save('Default')
    
    crt.Session.SetStatusText('Import Complete!')
    crt.Dialog.MessageBox('Done.')
    crt.Quit()

main()