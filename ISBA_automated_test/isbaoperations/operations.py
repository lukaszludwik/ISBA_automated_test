import subprocess
import time

import win32com.client
from automa.api import *

isba_application = None


def run_isba():
    """Run ISBA using Automa. Set global variable isba_application"""
    global isba_application
    isba_application = start("ISBA")


def kill_isba():
    """ Force kill ISBA application """
    kill(isba_application)


def close_isba():
    """ Close ISBA application using ALT + F4 """
    press(ALT + F4)


def enter_settings():
    """ Open ISBA settings window and set focus into it """
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys("s")
    time.sleep(1)
    switch_to(Window("Setting"))


def is_isba_running():
    """
    Check if ISBA process is running
    return True if ISBA process is running else return False
    """
    n = 0  # number of instances of the program running
    programs = [line.split() for line in subprocess.check_output("tasklist").splitlines()]
    [programs.pop(e) for e in [0, 1, 2]]
    for task in programs:
        if task[0] == "ISBA.exe":
            n += 1
    return True if n > 0 else False
