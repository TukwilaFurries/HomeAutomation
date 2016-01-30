#!/usr/bin/python

import unittest
from Framework import config

class TestLogging(unittest.TestCase):
    def testDIR(self):
        print "config.DIR.BASE: " + config.DIR.BASE
        print "config.DIR.FRAMEWORK: " + config.DIR.FRAMEWORK
        print "config.DIR.LOGS: " + config.DIR.LOGS
        print "config.DIR.MODS: " + config.DIR.MODS
        print "config.DIR.RGB: " + config.DIR.RGB

    def testFILE(self):
        print
        print "config.FILE.LOG.RGB: " + config.FILE.LOG.RGB

    def testPI(self):
        print
        print "config.PI.ADDR: " + config.PI.ADDR

    def testSERVER(self):
        print
        print "config.SERVER.ADDR: " + config.SERVER.ADDR
        print "config.SERVER.PORT: " + config.SERVER.PORT

    def testGLOBAL(self):
        print
        print "Current Logging Level: " + str(config.GLOBAL.LOG.LEVEL)
        print "Current Output Level: " + str(config.GLOBAL.LOG.OUTPUT)

    def testRGB(self):
        print
        print "config.RGB.PIN.R: " + str(config.RGB.PIN.R)
        print "config.RGB.PIN.G: " + str(config.RGB.PIN.G)
        print "config.RGB.PIN.B: " + str(config.RGB.PIN.B)

if __name__ == '__main__':
    unittest.main()
