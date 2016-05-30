#!/usr/bin/python

global moduleMailBoxes

class DIR:
    import os
    # Directory path variables
    BASE            = os.path.dirname(os.path.realpath(__file__))
    FRAMEWORK       = BASE + "/Framework"
    LOGS            = BASE + "/Logs"
    MODS            = BASE + "/Modules"
    RGB             = MODS + "/RGB"
    TEST            = BASE + "/UnitTests"
    TEST_FRAMEWORK  = TEST + "/Framework"
class FILE:
    class LOG:
        RGB = DIR.LOGS + "/rgb.out"
        FRAMEWORK = DIR.LOGS + "/framework.out"
        TEST = DIR.TEST_FRAMEWORK + "/logging.out"
class PI:
    # IP Addresses
    ADDR = "10.0.0.98"

class SERVER:
    ADDR = "10.0.0.99"
    PORT = ""
   
class NAMES:
    RGB          = "RGB"
    FRAMEWORK   = "FRAMEWORK"
    TEST        = "TEST"
class GLOBAL:
    class LOG:
        import Framework
        LEVEL = Framework.logging.LEVEL.VERBOSE
        OUTPUT = Framework.logging.OUTPUT.BOTH

class RGB:
    class PIN:
        R = 17
        G = 22
        B = 24

