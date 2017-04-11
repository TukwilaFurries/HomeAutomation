#!/usr/bin/python3



class DIR:
    import os.path as path

    # Directory path variables
    BASE            = path.dirname(path.realpath(__file__))
    FRAMEWORK       = BASE + "/Framework"
    LOGS            = BASE + "/Logs"
    MODS            = BASE + "/Modules"
    RGB             = MODS + "/RGB"
    TEST            = BASE + "/UnitTests"
    TEST_FRAMEWORK  = TEST + "/Framework"

class LOG:
    @staticmethod
    def getFrameworkLogLocation():
        return DIR.LOGS + "/framework.log"
    @staticmethod
    def getTestLogLocation():
        return DIR.LOGS + "/test.log"
    @staticmethod
    def getLogLevel():
        import logging
        return logging.DEBUG

    # To print to screen AS WELL AS logs
    @staticmethod
    def printToScreen():
        return True
        
# Delete this //maybe dont delete this? -sideway 1/2/17
class PI:
    # IP Addresses
    ADDR = "10.0.0.98"
# Delete this //maybe dont delete this? -sideway 1/2/17
class SERVER:
    ADDR = "10.0.0.99"
    PORT = ""
   
class NAMES:
    FRAMEWORK   = "FRAMEWORK"
    TEST        = "TEST"

# Delete this //maybe dont delete this? -sideway 1/2/17
class GLOBAL:
    class NETWORK:
        PIPORT = 15555


class MODULES:

    @classmethod
    def getClass(cls, inputID):
        if inputID == MODULES.NETWORK_CONTROLLER.ID:
            return MODULES.NETWORK_CONTROLLER.NAME

        if inputID == MODULES.RGB.ID:
            return MODULES.RGB.NAME
            
    
    class NETWORK_CONTROLLER:
        ID = 0
        NAME = "network_controller"

    class RGB:
        ID = 1
        NAME = "RGB"
