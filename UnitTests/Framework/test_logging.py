#!/usr/bin/python -s

import unittest
import config
from Framework.logging import test_log
from Framework.logging import LEVEL
from Framework.logging import OUTPUT
from Framework.logging import printLogLevel
def setLevelNone():
    config.GLOBAL.LOG.LEVEL = LEVEL.NONE
def setLevelStatus():
    config.GLOBAL.LOG.LEVEL = LEVEL.STATUS
def setLevelDebug():
    config.GLOBAL.LOG.LEVEL = LEVEL.DEBUG
def setLevelVerbose():
    config.GLOBAL.LOG.LEVEL = LEVEL.VERBOSE

def setOutputNone():
    config.GLOBAL.LOG.OUTPUT = OUTPUT.NONE
def setOutputStdout():
    config.GLOBAL.LOG.OUTPUT = OUTPUT.STDOUT
def setOutputFile():
    config.GLOBAL.LOG.OUTPUT = OUTPUT.FILE
def setOutputBoth():
    config.GLOBAL.LOG.OUTPUT = OUTPUT.BOTH

def confirmLog(file, level, msg):
    exp_module= "[TEST]"
    exp_level = "[" + printLogLevel(level) + "]"

    try:
        arr = open(file, 'r').readline().split()
        if (arr[2] == exp_level) and (arr[3] == exp_module) and (arr[4] == msg):
            return True;
    except Exception as ex:
        pass
    return False

class TestLogging(unittest.TestCase):
    def setUp(self):
        self.log_lvl = config.GLOBAL.LOG.LEVEL
        self.log_out = config.GLOBAL.LOG.OUTPUT

    def tearDown(self):
        config.GLOBAL.LOG.LEVEL = self.log_lvl
        config.GLOBAL.LOG.OUTPUT = self.log_out
        try:
            from os import remove
            remove(config.FILE.LOG.TEST)
        except:
            pass
          
    def testNoneToNone(self):
        setLevelNone()
        setOutputNone()
        test_log(LEVEL.NONE, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.NONE, self.id()))

    def testNoneToStdout(self):
        setLevelNone()
        setOutputStdout()
        test_log(LEVEL.NONE, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.NONE, self.id()))

    def testNoneToFile(self):
        setLevelNone()
        setOutputFile()
        test_log(LEVEL.NONE, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.NONE, self.id()))

    def testNoneToBoth(self):
        setLevelNone()
        setOutputBoth()
        test_log(LEVEL.NONE, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.NONE, self.id()))

    ##### Log Level Status Tests
    def testStatusToNone(self):
        setLevelStatus()
        setOutputNone()
        test_log(LEVEL.STATUS, self.id())

    def testStatusToStdout(self):
        setLevelStatus()
        setOutputStdout()
        test_log(LEVEL.STATUS, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.STATUS, self.id()))

    def testStatusToFile(self):
        setLevelStatus()
        setOutputFile()
        test_log(LEVEL.STATUS, self.id())
        self.assertTrue(confirmLog(config.FILE.LOG.TEST, LEVEL.STATUS, self.id()))
    
    def testStatusToBoth(self):
        setLevelStatus()
        setOutputBoth()
        test_log(LEVEL.STATUS, self.id())
        self.assertTrue(confirmLog(config.FILE.LOG.TEST, LEVEL.STATUS, self.id()))

    ##### Log Level Debug Tests
    def testDebugToNone(self):
        setLevelDebug()
        setOutputNone()
        test_log(LEVEL.DEBUG, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.DEBUG, self.id()))

    def testDebugToStdout(self):
        setLevelDebug()
        setOutputStdout()
        test_log(LEVEL.DEBUG, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.DEBUG, self.id()))

    def testDebugToFile(self):
        setLevelDebug()
        setOutputFile()
        test_log(LEVEL.DEBUG, self.id())
        self.assertTrue(confirmLog(config.FILE.LOG.TEST, LEVEL.DEBUG, self.id()))

    def testDebugToBoth(self):
        setLevelDebug()
        setOutputBoth()
        test_log(LEVEL.DEBUG, self.id())
        self.assertTrue(confirmLog(config.FILE.LOG.TEST, LEVEL.DEBUG, self.id()))

    ##### Log Level Verbose Tests
    def testVerboseToNone(self):
        setLevelVerbose()
        setOutputNone()
        test_log(LEVEL.VERBOSE, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.VERBOSE, self.id()))

    def testVerboseToStdout(self):
        setLevelVerbose()
        setOutputStdout()
        test_log(LEVEL.VERBOSE, self.id())
        self.assertFalse(confirmLog(config.FILE.LOG.TEST, LEVEL.VERBOSE, self.id()))

    def testVerboseToFile(self):
        setLevelVerbose()
        setOutputFile()
        test_log(LEVEL.VERBOSE, self.id())
        self.assertTrue(confirmLog(config.FILE.LOG.TEST, LEVEL.VERBOSE, self.id()))

    def testVerboseToBoth(self):
        setLevelVerbose()
        setOutputBoth()
        test_log(LEVEL.VERBOSE, self.id()) 
        self.assertTrue(confirmLog(config.FILE.LOG.TEST, LEVEL.VERBOSE, self.id()))

if __name__ == '__main__':
    unittest.main()
