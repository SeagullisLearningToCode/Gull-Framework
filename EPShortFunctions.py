"""
This file stores very simple functions with the sole purpose of de-bloating the Main.py file
"""
import os.path
import pygame

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
