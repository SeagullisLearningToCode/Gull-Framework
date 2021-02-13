"""
This file stores very simple functions with the sole purpose of de-bloating the Main.py file
"""
import os
import sys
import pygame
import getpass as gp

load = pygame.mixer.music

# p function
# reason: I am too lazy to keep using print("passed") so much times so I did this to make things easier on my self
def p():
    print("passed")

# sp function
# reason: same as the p function but made it faster to make a print statement by using a few characters
def sp(t: str = "passed",
       convert: int = 0): # This is to prevent Warnings/Errors
    if convert == 0: # None also default
        print(t)
    elif convert == 1: # Int --> Str
        if t is float or int:
            print(str(t))
    elif convert == 2: # Bool --> Str
        if t is bool:
            print(str(t))
    elif convert == 3: # List --> Str
        if t is list:
            print(str(t))
    else:
        return print(t)

# sps function
# Reason: easier and shorter
def sps(t: str):
    sp(f"passed {t}")

# Get Presence
# reason: shorten it up a bit with the os.path.exists
getpres = os.path.exists
def GetPresSpec(file: str):
    getpres = os.path.exists
    sp(t=getpres(file),
       convert=2)
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
    if error_type == 0: # FNFE
        sp(f"ERROR: {rfe}")
        raise FileNotFoundError
    elif error_type == 1: # FEE
        sp(f"ERROR: {rfe}")
        raise FileExistsError
    elif error_type == 2: # NEBW
        sp(f"WARNING: {rfe}")
    elif error_type == 3: # EP_RTI_E
        sp(f"ERROR: {rfe}")
        raise ValueError
    else:
        sp("Can't go higher than 1 at the moment...\n Sorry About that :(")
        raise ValueError



def Play(target: dict,
         name: str,
         loop: int):  # Plays the file which seems to work
    filename = target.get(name)
    load.load(filename)
    if loop != 1 or 0:
        raise ValueError
    load.play(loop)


def Que(target: dict,
        name: str):
    filename = target.get(name)
    load.queue(filename)


def QuesFromDict(target: dict): # takes the values from the target and qeue
    names = target
    for i in names:
        Que(names, i)
        print(names, i)

def EccoPyDevLogStuff(filepath: str = "/Documents/SIS/EccoPY/LOGS/", # Possibly returns as error
                      textfile: str = "DeveloperLog", # Filename.ext
                      file_type: str = ".log", # Required
                      lmt_filesize: float = 0x164210, # EXPERIMENTAL
                      isThisEnabled: bool = True): # Skip function
    # Init/
    #   Args/
    #       Vars/
    #           STR/
    gun = gp.getuser()
    fp = filepath
    tf = textfile
    #           INT/
    #           FLOATS/
    lfs = lmt_filesize
    # Abs/
    #   Args/
    if os.path.exists(f"/Users/{gun}{fp}") is False:
        os.makedirs(
            f"/Users/{gun}{fp}"
        )
    else:
        pass
    if os.path.exists(f"/Users/{gun}{fp}{tf}{file_type}") is False:
        sys.stderr = open(f"/Users/{gun}{fp}{tf}", "w+")
    else:
        pass
    if isThisEnabled == True:
        if not os.path.getsize(f"/Users/{gun}{fp}{tf}") >= lfs:
            sys.stdout = open(f"/Users/{gun}{fp}{tf}", "w+")
            if os.path.getsize(f"/Users/{gun}{fp}/{tf}") >= lfs:
                sys.stdout.close()
    else:
        pass

def EccoPyDevLogStuff_ERRORS(filepath: str = "/Documents/SIS/EccoPY/LOGS/", # Possibly returns as error
                             textfile: str = "DeveloperLog", # Filename.ext
                             file_type: str = ".log",
                             lmt_filesize: float = 0x1684210, # EXPERIMENTAL
                             isThisEnabled: bool = True): # Skip function
    # Init/
    #   Args/
    #       Vars/
    #           STR/
    gun = gp.getuser()
    fp = filepath
    tf = textfile
    #           INT/
    #           FLOATS/
    lfs = lmt_filesize
    # Abs/
    #   Args/
    if os.path.exists(f"/Users/{gun}{fp}") is False:
        os.makedirs(
            f"/Users/{gun}{fp}"
        )
    else:
        pass
    if os.path.exists(f"/Users/{gun}{fp}{tf}-err{file_type}") is False:
        sys.stderr = open(f"/Users/{gun}{fp}{tf}-err{file_type}", "w+")
    else:
        pass
    if isThisEnabled == True:
        if not os.path.getsize(f"/Users/{gun}{fp}{tf}-err{file_type}") >= lfs:
            sys.stderr = open(f"/Users/{gun}{fp}{tf}-err{file_type}", "w+")
            if os.path.getsize(f"/Users/{gun}{fp}/{tf}-err{file_type}") >= lfs:
                sys.stderr.write("Done Writing...")
                sys.stderr.close()
    else:
        pass
