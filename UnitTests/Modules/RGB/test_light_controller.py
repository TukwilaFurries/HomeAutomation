#!/usr/bin/python

import unittest
from Modules.RGB import light_controller
from Modules.RGB import light_model
import time

class  test_light_control(unittest.TestCase):
    def test(self):
        piLights = light_controller.PiLights()
        pattern = light_model.Pattern()
        pattern.setBrightLevel(255)
        piLights.setPattern(pattern)
        time.sleep(5)
        piLights.killProgram()

class myProgram:
    def __init__(self):
        self.piLights = light_controller.piLights()
        self.umColors = 3
        self.fadeTime = 1
        self.loopTime = 20
        self.brightLevel = 255 
        self.colors = [ [1, 11, 111], [2, 22, 222], [3, 33, 333]]
        self.pattern = Pattern(self.numColors, self.fadeTime, self.loopTime, self.brightLevel, self.colors)

    def begin(self):
        self.piLights.setPattern(pattern)
        while True:
            try:
                pass
            except KeyboardInterrupt:
                print "Quitting"
                self.piLights.killProgram()
                sys.exit()
if __name__ == '__main__':
    #unittest.main()
    p = myProgram
    p.begin()
