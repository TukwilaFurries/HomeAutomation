#!/usr/bin/python

import unittest
import config 
import Modules.RGB.light_model
from Modules.RGB import Pattern
from Modules import RGB
class TestLightModel(unittest.TestCase):
    def setUp(self):
        self.numColors = 3
        self.fadeTime = 10
        self.loopTime = 20
        self.brightLevel = 255 
        self.colors = [ [1, 11, 111], [2, 22, 222], [3, 33, 333]]
        self.pattern = Pattern(self.numColors, self.fadeTime, self.loopTime, self.brightLevel, self.colors)

    def test_constructor(self):
        self.assertEqual(self.numColors, self.pattern.numColors)
        self.assertEqual(self.fadeTime, self.pattern.fadeTime)
        self.assertEqual(self.loopTime, self.pattern.loopTime)
        self.assertEqual(self.brightLevel, self.pattern.brightLevel)
        self.assertItemsEqual(self.colors, self.pattern.colors)
        
    def test_getBrightLevel(self):
        self.assertEqual(self.brightLevel, self.pattern.getBrightLevel())
    def test_getColors(self):   
        self.assertEqual(self.colors, self.pattern.getColors())
    def test_getColorR(self):
        for i in range (0, 3):
            self.assertEqual(self.colors[i][RGB.SPECTRUM.R], self.pattern.getColorR(i))
    def test_getColorG(self):
        for i in range(0, 3):
            self.assertEqual(self.colors[i][RGB.SPECTRUM.G], self.pattern.getColorG(i))
    def test_getColorB(self):
        for i in range(0, 3):
            self.assertEqual(self.colors[i][RGB.SPECTRUM.B], self.pattern.getColorB(i))
    def test_getFadeTime(self):
        self.assertEqual(self.fadeTime, self.pattern.getFadeTime())
    def test_getLoopTime(self):
        self.assertEqual(self.loopTime, self.pattern.getLoopTime())
    def test_getNumColors(self):
        self.assertEqual(self.numColors, self.pattern.getNumColors())

if __name__ == '__main__':
    unittest.main()
