#!/usr/bin/python3
import logging
import config
import sys

class HomeAutomationLogging:
    def __init__(self, module, log_file):
        extra = {'mod_name' : module}
        self.log = logging.getLogger(module)
        self.formatter = logging.Formatter('[%(asctime)s] [%(mod_name)s] : %(message)s')
        self.fileHandler = logging.FileHandler(log_file, mode='w')
        self.fileHandler.setFormatter(self.formatter)
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(self.formatter)
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.addHandler(self.fileHandler)
        self.log.addHandler(self.streamHandler)
        self.log = logging.LoggerAdapter(self.log, extra)

    # Algorithm Output - Should only be used during development, and deleted entirely during production
    def debug(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.LEVEL)
        self.log.debug(message)

    # Basic status messages signifying properly working product
    def info(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.LEVEL)
        self.log.info(message)

    # Warnings that don't prevent product from working properly
    def warn(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.LEVEL)
        self.log.warn(message)

    # An error that can have adverse affects if not caught properly
    def error(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.LEVEL)
        self.log.error(message)

    # Something has gone wrong, and needs to be dealt with immediately
    def critical(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.LEVEL)
        self.log.critical(message)

if __name__ == '__main__':
    import config
    import logging
    TestLog=HomeAutomationLogging("rgb", config.LOG().getTestLogLocation())
    config.LOG.LEVEL = logging.DEBUG

    #config.LOG.LEVEL=logging.DEBUG
    TestLog.debug("DEBUG")

    #config.LOG.LEVEL=logging.CRITICAL
    TestLog.info("INFO")

    #config.LOG.LEVEL=logging.WARN
    TestLog.warn("WARN")

    #config.LOG.LEVEL=logging.ERROR
    TestLog.error("ERROR")

    #config.LOG.LEVEL=logging.CRITICAL
    TestLog.critical("CRITICAL")

    FrameworkLog = HomeAutomationLogging("framework", config.LOG().getFrameworkLogLocation())
    FrameworkLog.debug("DEBUG")
    FrameworkLog.info("INFO")
    FrameworkLog.warn("WARN")
    FrameworkLog.error("ERROR")
    FrameworkLog.critical("CRITICAL")




















##############################################################################
#
# 
#
#############################################################################
#class LEVEL:
#    NONE = 0    # No messages printed
#    STATUS = 1   # Status changes
#    DEBUG = 2   # Logic decisions, status changes
#    VERBOSE = 3 # Code branches, logic decisions, status changesa

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
#class OUTPUT:
#    NONE = 0
#    STDOUT = 1
#    FILE = #2
#    BOTH = 3

#def printLogLevel(lvl):
#    if lvl == LEVEL.NONE#:
#        return "NONE"
#    if lvl == LEVEL.STATUS:
#        return "STATUS"
#    if lvl == LEVEL.DEBUG:
#        return "DEBUG"
#    if lvl == LEVEL.VERBOSE:
#        return "VERBOSE"


#def printLogOutput(lvl#):
#    if lvl == OUTPUT.NONE:
#        return "NONE"
#    if lvl == OUTPUT.STDOUT:
#        return "STDOUT"
#    if lvl == OUTPUT.FILE:
#        return "FILE"
#    if lvl == OUTPUT.BOTH:
#        return "BOTH"

#def get_log_stamp(module):
#    import time
#    import #config
#    return ("[" + module + "] ")

##### The workers
#def log(level, message, module, file):
#    import config
#    if ( isinstance(level, int) == False):
#        print("Level is not an integer#")
#
#    if ( isinstance(config.GLOBAL.LOG.LEVEL, int) == False):
#        print("Global level is not an integer")
#
#    if ( isinstance(config.GLOBAL.LOG.OUTPUT, int) == False):
#        print("Output is not an integer")

#    if config.GLOBAL.LOG.LEVEL == LEVEL.NONE:
#        print("EXIT Logging Disabled (%s)" % message)
#        return

#    if config.GLOBAL.LOG.OUTPUT == OUTPUT.NONE:
#        print("EXIT Output Is None (%s) " % message)
#        return 

#    if config.GLOBAL.LOG.LEVEL < level:
#        print("EXIT Level not high enough (%s) " % message)
#        return

#    if (config.GLOBAL.LOG.OUTPUT == OUTPUT.BOTH) or (config.GLOBAL.LOG.OUTPUT == OUTPUT.STDOUT#):
#        print(get_log_stamp(module) + message)
#
#    if (config.GLOBAL.LOG.OUTPUT == OUTPUT.BOTH) or (config.GLOBAL.LOG.OUTPUT == OUTPUT.FILE):
#        f1 = open(file, 'a+')
#        f1.write(get_log_stamp(module) + message + "\n")

#def rgb_log(level, message):
#    import logging
#    import config
#    logging.basicConfig(filename=config.FILE.LOG.RGB, level=config.LOG.LEVEL)
#    log(level, message, config.NAMES.RGB, config.FILE.LOG.RGB)

#def framework_log(level, message):
#    import config
#    log(level, message, config.NAMES.FRAMEWORK, config.FILE.LOG.FRAMEWORK)  

#def test_log(level, message):
#    import config
#    log(level, message, config.NAMES.TEST, config.FILE.LOG.TEST)


#def log_rgb_debug(module, message):
#    import logging
#    import config
#    logging.basicConfig(filename=config.FILE.LOG.RGB, level=config.LOG.LEVEL)
#    logging.debug(get_log_stamp(module) + message)

#3def log_rgb_info(module, message):
#    import logging
#    import config
#    logging.basicConfig(filename=config.FILE.LOG.RGB, level=config.LOG.LEVEL)
#    logging.info(get_log_stamp(module) + message)

#def log_rgb_warn(module, message):
#    import logging
#    import config
#    logging.basicConfig(filename=config.FILE.LOG.RGB, level=config.LOG.LEVEL)
#    logging.warn(get_log_stamp(module) + message)

#def log_rgb_error(module, message):
#    import logging
#    import config
#    logging.basicConfig(filename=config.FILE.LOG.RGB, level=config.LOG.LEVEL)
#    logging.error(get_log_stamp(module) + message)

#ef log_rgb_critical(module, message):
#    import logging
#    import config
#    logging.basicConfig(filename=config.FILE.LOG.RGB, level=config.LOG.LEVEL#)
#    logging.critical(get_log_stamp(module) + message)

#if __name__ == '__main__':
#    import config
#    import logging
#
#    config.LOG.LEVEL=logging.DEBUG
#    log_rgb_debug("RGB", "DEBUG#")
#
#    config.LOG.LEVEL=logging.INFO
#    log_rgb_info("RGB", "INFO")
#
#    config.LOG.LEVEL=logging.WARN
#    log_rgb_warn("RGB", "WARN")
#
#    config.LOG.LEVEL=logging.ERROR
#    log_rgb_error("RGB", "ERROR")
#
#    config.LOG.LEVEL=logging.CRITICAL
#    log_rgb_critical("RGB", "CRITICAL")
#
