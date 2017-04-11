#!/usr/bin/python3
import logging
import config
import sys

class HomeAutomationLogging:
    def __init__(self, module, log_file):
        self.log = logging.getLogger(module)
        self.log_file = log_file
        self.module = module
        self.initialize()

    def initialize(self):
        self.formatter = logging.Formatter('[%(asctime)s] [%(mod_name)s] : %(message)s')
        self.fileHandler = logging.FileHandler(self.log_file, mode='w')
        self.fileHandler.setFormatter(self.formatter)
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(self.formatter)
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.addHandler(self.fileHandler)
        self.log.addHandler(self.streamHandler)
        extra = {'mod_name' : self.module}
        self.log = logging.LoggerAdapter(self.log, extra)

    # Algorithm Output - Should only be used during development, and deleted entirely during production
    def debug(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.debug(message)
    # Basic status messages signifying properly working product
    def info(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.info(message)

    # Warnings that don't prevent product from working properly
    def warn(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.warn(message)

    # An error that can have adverse affects if not caught properly
    def error(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.error(message)

    # Something has gone wrong, and needs to be dealt with immediately
    def critical(self, message):
        import logging
        import config
        self.log.setLevel(config.LOG.getLogLevel())
        self.log.critical(message)

if __name__ == '__main__':
    import config
    import logging
    TestLog=HomeAutomationLogging("rgb", config.LOG().getTestLogLocation())
    TestLog.initialize()
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

    TestLog2=HomeAutomationLogging("rgb", config.LOG.getTestLogLocation());
    TestLog2.initialize()
    config.LOG.LEVEL = logging.DEBUG
    TestLog.debug("DEBUGGING A THING")
    TestLog2.debug("DEBUGGING ANOTHER THING")

