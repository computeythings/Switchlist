import os, subprocess, time, json, shutil, logging, pathlib
logging.basicConfig(level=logging.INFO,
    format='%(levelname)s: %(asctime)s - %(message)s')

def get_securecrt():
    '''
    Locates SecureCRT on host device. Local install vs System Install
    '''

    sysinstalldir = os.getenv("PROGRAMFILES") + "\\VanDyke Software\\SecureCRT"
    if os.path.exists(sysinstalldir):
        logging.debug(f"System Directory: '{sysinstalldir}'")
        sysdata = subprocess.check_output(f"dir \"{sysinstalldir}\"", shell=True).decode()
        logging.debug(f"System Files:{sysdata}")
        if "SecureCRT.exe" in sysdata:
            return sysinstalldir + '\\SecureCRT.exe'
        
    userinstalldir = os.getenv("LOCALAPPDATA") + "\\VanDyke Software\\SecureCRT"
    if os.path.exists(userinstalldir):
        logging.debug(f'Local AppData: {userinstalldir}')
        userdata = subprocess.check_output(f"dir \"{userinstalldir}\"", shell=True).decode()
        logging.debug(f"User Files:{userdata}")
        if "SecureCRT.exe" in userdata:
            return userinstalldir + "\\SecureCRT.exe"
        
    userinstalldir = os.getenv("LOCALAPPDATA") + "\\VanDyke Software\\Clients\\SecureCRT"
    if os.path.exists(userinstalldir):
        logging.debug(f'Local AppData: {userinstalldir}')
        userdata = subprocess.check_output(f"dir \"{userinstalldir}\"", shell=True).decode()
        logging.debug(f"User Files:{userdata}")
        if "SecureCRT.exe" in userdata:
            return userinstalldir + "\\SecureCRT.exe"
        
    sysinstalldir = os.getenv("PROGRAMFILES") + "\\VanDyke Software\\Clients\\SecureCRT"
    if os.path.exists(sysinstalldir):
        logging.debug(f"System Directory: '{sysinstalldir}'")
        sysdata = subprocess.check_output(f"dir \"{sysinstalldir}\"", shell=True).decode()
        logging.debug(f"System Files:{sysdata}")
        if "SecureCRT.exe" in sysdata:
            return sysinstalldir + '\\SecureCRT.exe'
        
    logging.warn("Unable to locate SecureCRT install")
    return None

def temporary_switchlist(switchlist):
    '''
    Creates a temporary switch list JSON file to import into SecureCRT
    '''
    tempfile = os.getenv("TEMP") + f"\\switchlist_{int(time.time())}.json"
    with open(tempfile, 'w') as listfile:
        json.dump(switchlist, listfile, indent=2)
    return tempfile

def temporary_importscript():
    '''
    Creates a temprorary directory on the host device containing the SecureCRT import script and required resources
    '''
    tempdir = os.getenv("TEMP") + f"\\import_{int(time.time())}"
    crtdir = f"{pathlib.Path().resolve()}\\SecureCRT"
    crtdata = subprocess.check_output(f"dir \"{crtdir}\"", shell=True).decode()
    logging.debug(f"CRT Files:{crtdata}")
    if not os.path.exists(tempdir):
        shutil.copytree(crtdir, tempdir)
    return tempdir + "\\session_import.py"

def update_localhost(switchlist):
    '''
    Updates SecureCRT sessions on server (non-blocking)
    '''
    logging.info('Running update script on local SecureCRT instance.')
    run_command = [get_securecrt(), "/script", temporary_importscript(), "/arg", temporary_switchlist(switchlist)]
    subprocess.Popen(run_command)