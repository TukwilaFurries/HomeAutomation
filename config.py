#!/usr/bin/python

import os
from Framework.logging import LEVEL
from Framework.logging import OUTPUT

class DIR:
    # Directory path variables
    BASE = os.path.dirname(os.path.realpath(__file__))
    FRAMEWORK   = BASE + "/Framework"
    LOGS        = BASE + "/Logs"
    MODS        = BASE + "/Modules"
    RGB         = MODS + "/RGB"

class FILE:
    class LOG:
        RGB = DIR.LOGS + "/rgb.out"

class PI:
    # IP Addresses
    ADDR = "10.0.0.98"

class SERVER:
    ADDR = "10.0.0.99"
    PORT = ""
   
class NAMES:
    RGB          = "RGB"

class GLOBAL:
    class LOG:
        LEVEL = LEVEL.STATUS
        OUTPUT = OUTPUT.STDOUT

class RGB:
    class PIN:
        R = 17
        G = 22
        B = 24
