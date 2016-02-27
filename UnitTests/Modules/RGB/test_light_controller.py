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

if __name__ == '__main__':
    unittest.main()
