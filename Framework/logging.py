#!/usr/bin/python
import time

class LEVEL:
    NONE = 0    # No messages printed
    STATUS = 1   # Status changes
    DEBUG = 2   # Logic decisions, status changes
    VERBOSE = 3 # Code branches, logic decisions, status changesa
            
class OUTPUT:
    NONE = 0
    STDOUT = 1
    FILE = 2
    BOTH = 3


def get_log_stamp(module):
    return (time.strftime("%d/%m/%Y %H:%M:%S") + " [" + module + "] ")

##### The workers
def log(level, message, module, file):
    import config
    #print "Configured Level: " + str(config.GLOBAL.LOG.LEVEL)
    #print "Debug Level: " + str(level)
    return
    if config.GLOBAL.LOG.LEVEL < level:
        return
    if (config.GLOBAL.LOG.LEVEL == OUTPUT.STDOUT) or (config.GLOBAL.LOG.LEVEL == OUTPUT.BOTH):
        print get_log_stamp(module) + message
    if (config.GLOBAL.LOG.LEVEL == OUTPUT.FILE) or (config.GLOBAL.LOG.LEVEL == OUTPUT.BOTH):
        f1 = open(file, 'w+')
        f1.write(get_log_stamp(module) + message)

def rgb_log(level, message):
    import config
    log(level, message, config.NAMES.RGB, config.FILE.LOG.RGB) 

##### DEPRECATED DO NOT USE #####
def RGB_LOG(level, message):
    rgb_log(level, message)
