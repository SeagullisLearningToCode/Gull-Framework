"""
████████████████████████████████████████████████████████████████████▓░░░░░░░░░░░░░░░░░░░░░
█████████████████████▒░▒▒▒▒▒▒▓▓█████████████████████████████████████▓░░░░░░░░░░░░░░░░░░░░░
███████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░▒▓▓███████████████████████████▒░░░░░░░░░░░░░░░░░░░░░
████████████▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░
██████████▓░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒░▒░░░░░░░▒██████████████████▓▒░░░░░░░░░░░░░░░░░░░░
█████████▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒████████████████▓▒░░░░░░░░░░░░░░░░░░░░
███████▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒██████████████▓▒░░░░░░░░░░░░░░░░░░░░
████▓░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░▒███████████▓▓▓░░░░░░░░░░░░░░░░░░░░
████▓▒░░░░░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████▓▓▓▒▒▒▒▒▒▒░░▓███████████▓░░░░░░░░░░░░░░░░░░░░
████▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████▓▒▒▒▒▒▒▒▒▒░░████████▓█▓░░░░░░░░░░░░░░░░░░░░
█▓▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████▓▓▒▒▒▒▒▒▒▒▒▒▒░▒▓██████▓▒░░░░░░░░░░░░░░░░░░░░
█▓▓▓▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒████▒░░░░░░░░░░░░░░░░░░░░
███▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▓▓▓░░░░░░░░░░░░░░░░░░░░
███▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░
██▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░
██▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▓█▓▓▓▓▓▒▒▒▒▒▒░░░░
█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█▓██████████▓▓▒▒▒▒▒░░░
▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█████████▓▓▓▓████████████▓▒▒▒░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████████▓░▒▒▓███████████▓▒▒░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████████████░░░░░░░▒▒▒▓▓▒▒▓▒▒▒░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████████████▓░░░░░░░░░░░░░░░░░▒░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████▓▓▓▒░░░░░░░░░░░░░░░░░░░
 __                     ___  __              ___       __   __
/ _` |  | |    |       |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/
\__> \__/ |___ |___    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \
                                                    Version: 1 Beta (Public Ver)


This file stores very simple functions with the sole purpose of de-bloating the Main.py file
This file is also makes stating certain things faster and possibly easier.
"""

import os
import sys
import pygame
import getpass as gp
from datetime import *
from random import *
from configparser import *

load = pygame.mixer.music

# Today's Date
td = date.today()

# print(type(td)) # Get td's return type
td_c_s = str(td)  # Converts the current date into a String
td_c_s_yo = td_c_s[0:4]  # Get year only
# Today's Time
tt = datetime.now()


# p function
# reason: I am too lazy to keep using print("passed") so much times so I did this to make things easier on my self
def p():
    print("passed")


# sp function
# reason: same as the p function but made it faster to make a print statement by using a few characters
def sp(t="passed"):  # This is to prevent Warnings/Errors
    print(t)


# sps function
# Reason: easier and shorter
def sps(t: str):
    sp(f"passed {t}")


# Get Presence
# reason: shorten it up a bit with the os.path.exists
def GetPresSpec(file: str):
    getpres = os.path.exists
    sp(f"{getpres(file)}")


# Raise Custom Error Function (RCEF)
"""
Refrences
----------
rfe: String
et: which error do you want to raise
    Values:
            0 = File Not Found Error (ERROR)
            1 = File Exists Error (ERROR
            2 = Not an Error but a Warning (WARNING)
            3 = EccoPY_RenderTypeInvaild_Error (ERROR)
"""


def RCE(rfe: str, et: int):
    error_type = et
    if error_type == 0:  # FNFE
        sp(f"ERROR: {rfe}")
        raise FileNotFoundError
    elif error_type == 1:  # FEE
        sp(f"ERROR: {rfe}")
        raise FileExistsError
    elif error_type == 2:  # NEBW
        sp(f"WARNING: {rfe}")
    elif error_type == 3:  # EP_RTI_E
        sp(f"ERROR: {rfe}")
        raise ValueError
    else:
        sp("Can't go higher than 1 at the moment...\n Sorry About that :(")
        raise ValueError


class GF_MUSICPLAYER_DICT_FORM(object):
    def __init__(self):
        sp("Gull: Instruments here and some scripts ready!")
        # Func/
        #   Args/
        #       Vars/
        #           Dict/

    def play(self,
             target: dict,
             name: str,
             loop: int):
        filename = target.get(name)
        load.load(filename)
        if loop != 1 or 0:
            if randint(0, 100) == 1:
                sp(f"Gull: Sorry I can't do that option {loop}, maybe tell me a yes or a no, or in what I can read a 1 or a 0 (representing on or off).")
            raise ValueError
        elif loop == 1:
            sp(f"Gull: I will be playing '{filename}' without stopping, hopefully I don't get tired")
        elif loop == 0:
            sp(f"Gull: I will be playing '{filename}' alright")
        load.play(loop)

    def que(self,
            target: dict,
            name: str):
        filename = target.get(name)
        sp(f"Gull: Putting {filename} on my list")
        load.queue(filename)

    def queFromDict(self, target: dict):  # takes the values from the target and qeues them
        names = target
        for i in names:
            sp(f"Gull: Putting {i} from your written list into my list")
            self.que(names, i)


class GF_DEVLOG(object):
    def __init__(self,
                 filepath: str = "/Documents/SIS/EccoPY/LOGS/",
                 textfile: str = "DEVELOPERLOG",
                 filetype: str = ".log",
                 limit_fs: float = 0x164210,
                 isThisEnabled: bool = True):
        # Init/
        #   Args/
        #       Vars/
        #           STR/
        self.fp = (filepath)
        self.tf = (textfile)
        self.ft = (filetype)
        #           Float/
        self.lfs = (limit_fs)
        #           Booleans/
        self.ise = isThisEnabled
        #   STATEMENTS/
        #       Vars/
        #           STR/
        self.gun = gp.getuser()
        # ;Seagull
        sp("Gull: I am here...")

    def RECORD_CONSOLE(self, what):
        if what is not sys.stderr or sys.stdout or sys.stdin:
            sp(f"Gull: ARGUMENT OF RECORD WHICH IS {what} ISN'T 'sys.stderr', 'sys.stdout OR 'sys.stdin'\n SOLUTION: Try changing 'what' to one of those options")
            raise ValueError
        if os.path.exists(f"/Users/{self.gun}{self.fp}") is False:
            os.makedirs(
                f"/Users/{self.gun}{self.fp}"
            )
        if os.path.exists(f"/Users/{self.gun}{self.fp}{self.tf + str(what)}{self.ft}") is False:
            what = open(f"/Users/{self.gun}{self.fp}{self.tf + str(what)}", "w+")
        if self.ise == True:
            sp(f"Gull: I am going to write down whatever is in the console ok since you said that you want me to record what happens to a file \nIsThisRecording: {self.ise}")
            if not os.path.getsize(f"/Users/{self.gun}{self.fp}{self.tf}") >= self.lfs:
                what = open(f"/Users/{self.gun}{self.fp}{self.tf}", "w+")
                if os.path.getsize(f"/Users/{self.gun}{self.fp}/{self.tf}") >= self.lfs:
                    what.close()
        else:
            if randint(0, 25) == 1:
                sp("Ok")


class GF_WRITE_SETTING_FILES(object):
    def __init__(self):
        sp("Gull: I guess we'll be writting important files then")
        # Init/
        #   Args/
        #       Vars/
        #           STR/

    def writeSettingsFile(self,
                          dir: str = "/Documents/Seagulls/EccoPY/",
                          name: str = "Settings"):
        d = dir
        n = name
        gun = gp.getuser()
        subdir = f"{gun}/EP_S/"
        getdir = f"/Users/{gun}{d}{subdir}"

        if os.path.exists(getdir) is False:
            os.makedirs(getdir)
        elif os.path.exists(f"{getdir}/{n}.ini") is False:
            newfile = open(f"{getdir}/{n}.ini", "w+")  # Creates new file
            newfile.close()


class GF_MAPPING(object):
    def __init__(self):
        sp("Gull: Paint.exe and paper is ready")
        # Init/
        #   Args/
        #       Vars/
        #           STR/

    def loadMap(self, filepath):
        f = open(filepath, "r")
        data = f.read()
        f.close()
        data = data.split('\n')
        gmap = []
        for bit in data:
            gmap.append(list(bit))
        return gmap


class GF_INIT(object):
    def __init__(self, assembly_mode: bool = False):
        sp("\nGull Framework Beta \n      By SeagullinSeagulls\n")
        # Init/
        #   Args/
        #       Vars/
        #           Booleans/
        self.enable_assembly_mode = (assembly_mode)
        #   I/
        if self.enable_assembly_mode == True:
            self.m = GF_MAPPING()  # Deals with mapping
            self.dl = GF_DEVLOG()  # Logs stuff
            self.wsf = GF_WRITE_SETTING_FILES()  # Writes INI files
            self.mpdf = GF_MUSICPLAYER_DICT_FORM()  # Deals with playing music from dicts
        else:
            self.map = GF_MAPPING()
            self.log = GF_DEVLOG()
            self.set = GF_WRITE_SETTING_FILES()
            self.musicPlayer = GF_MUSICPLAYER_DICT_FORM()

        #if self.enable_assembly_mode == True:
        #    del self.map
        #    del self.log
        #    del self.set
        #    del self.musicPlayer
        #else:
        #    pass


GF = GF_INIT(True)
