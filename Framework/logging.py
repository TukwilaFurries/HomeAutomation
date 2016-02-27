#!/usr/bin/python
##############################################################################
#
# 
#
#############################################################################
class LEVEL:
    NONE = 0    # No messages printed
    STATUS = 1   # Status changes
    DEBUG = 2   # Logic decisions, status changes
    VERBOSE = 3 # Code branches, logic decisions, status changesa

##############################################################################
# config.OUTPUT
#   Description:
#       Where will the logs print to
#   Options:
#       NONE: All logging will be dropped
#       STDOUT: All logging will go to stdout
#       FILE:   All logging will go to the corresponding log file
#       BOTH:   All logging will go to stdout and corresponding log file
#############################################################################           
class OUTPUT:
    NONE = 0
    STDOUT = 1
    FILE = 2
    BOTH = 3

def printLogLevel(lvl):
    if lvl == LEVEL.NONE:
        return "NONE"
    if lvl == LEVEL.STATUS:
        return "STATUS"
    if lvl == LEVEL.DEBUG:
        return "DEBUG"
    if lvl == LEVEL.VERBOSE:
        return "VERBOSE"


def printLogOutput(lvl):
    if lvl == OUTPUT.NONE:
        return "NONE"
    if lvl == OUTPUT.STDOUT:
        return "STDOUT"
    if lvl == OUTPUT.FILE:
        return "FILE"
    if lvl == OUTPUT.BOTH:
        return "BOTH"

def get_log_stamp(module):
    import time
    import config
    return (time.strftime("%d/%m/%Y %H:%M:%S") + " [" + printLogLevel(config.GLOBAL.LOG.LEVEL) + "]"+ " [" + module + "] ")

##### The workers
def log(level, message, module, file):
    import config
    if ( isinstance(level, int) == False):
        print "Level is not an integer"

    if ( isinstance(config.GLOBAL.LOG.LEVEL, int) == False):
        print "Global level is not an integer"

    if ( isinstance(config.GLOBAL.LOG.OUTPUT, int) == False):
        print "Output is not an integer"

    if config.GLOBAL.LOG.LEVEL == LEVEL.NONE:
        #print "EXIT Logging Disabled (%s)" % message
        return

    if config.GLOBAL.LOG.OUTPUT == OUTPUT.NONE:
        #print "EXIT Output Is None (%s) " % message
        return 

    if config.GLOBAL.LOG.LEVEL < level:
        #print "EXIT Level not high enough (%s) " % message
        return

    if (config.GLOBAL.LOG.OUTPUT == OUTPUT.BOTH) or (config.GLOBAL.LOG.OUTPUT == OUTPUT.STDOUT):
        print get_log_stamp(module) + message

    if (config.GLOBAL.LOG.OUTPUT == OUTPUT.BOTH) or (config.GLOBAL.LOG.OUTPUT == OUTPUT.FILE):
        f1 = open(file, 'a+')
        f1.write(get_log_stamp(module) + message + "\n")

def rgb_log(level, message):
    import config
    log(level, message, config.NAMES.RGB, config.FILE.LOG.RGB)

def framework_log(level, message):
    import config
    log(level, message, config.NAMES.FRAMEWORK, config.FILE.LOG.FRAMEWORK)  

def test_log(level, message):
    import config
    log(level, message, config.NAMES.TEST, config.FILE.LOG.TEST)

##### DEPRECATED DO NOT USE #####
def RGB_LOG(level, message):
    rgb_log(level, message)
