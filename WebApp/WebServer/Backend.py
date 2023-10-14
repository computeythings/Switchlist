from tkinter import messagebox, filedialog
import os, subprocess, time, json, shutil, logging, pathlib

darkthemepath = 'cisco_dark.ini' 
lightthemepath = 'cisco_light.ini'
logger = logging.getLogger(__name__)

def get_securecrt():
    '''
    Locates SecureCRT on host device. Local install vs System Install
    '''

    install_dir = [
        os.getenv("PROGRAMFILES") + "\\VanDyke Software\\SecureCRT",
        os.getenv("PROGRAMFILES") + "\\VanDyke Software\\Clients\\SecureCRT",
        os.getenv("LOCALAPPDATA") + "\\VanDyke Software\\SecureCRT",
        os.getenv("LOCALAPPDATA") + "\\VanDyke Software\\Clients\\SecureCRT"
    ]

    for dir in install_dir:
        if os.path.exists(dir):
            logger.info(f"Checking directory: '{dir}'")
            sysdata = subprocess.check_output(f"dir \"{dir}\"", shell=True).decode()
            logger.debug(f"System Files:{sysdata}")
            if "SecureCRT.exe" in sysdata:
                logger.info(f"Found SecureCRT install at: {dir}")
                return dir + "\\SecureCRT.exe"
        
    logger.warn("Unable to locate SecureCRT install")
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
    return f"{pathlib.Path().resolve()}\\SecureCRT\\session_import.py"

def update_localhost(switchlist):
    '''
    Updates SecureCRT sessions on server (non-blocking)
    '''
    logger.info('Running update script on local SecureCRT instance.')
    securecrt = get_securecrt()
    if securecrt is None:
        messagebox.showwarning("Could not locate SecureCRT", "Please select SecureCRT .exe file")
        securecrt = filedialog.askopenfilename(title="Please Select SecureCRT",filetypes=[("exe files", "*.exe")])
    if securecrt is None:
        logger.warn("Could not locate SecureCRT: skipping update")
        return
    run_command = [securecrt, "/script", temporary_importscript(), "/arg", temporary_switchlist(switchlist)]
    subprocess.Popen(run_command)

def copy_themes():
    '''
    Copy themes into local user's secureCRT keyword directory
    '''
    shutil.copyfile(f"{pathlib.Path().resolve()}\\SecureCRT\\{darkthemepath}", f'C:\\Users\\{pathlib.Path.home()}\\AppData\\Roaming\\VanDyke\\Config\\Keywords\\{darkthemepath}')
    shutil.copyfile(f"{pathlib.Path().resolve()}\\SecureCRT\\{lightthemepath}", f'C:\\Users\\{pathlib.Path.home()}\\AppData\\Roaming\\VanDyke\\Config\\Keywords\\{lightthemepath}')