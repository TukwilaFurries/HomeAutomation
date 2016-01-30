#!/usr/bin/python

import unittest
from Modules.RGB import *
import time

class  test_light_control(unittest.TestCase):
    def test(self):
        piLights = light_controller.PiLights()
        pattern = Pattern()
        pattern.setBrightLevel(255)
        piLights.setPattern(pattern)
        time.sleep(5)
        piLights.killProgram()

if __name__ == '__main__':
    unittest.main()
