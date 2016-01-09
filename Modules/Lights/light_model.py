#!/usr/bin/python

class Pattern:
    numColors = 0
    fadeTime = 0
    loopTime = 0
    brightLevel = 0
    colors = []

    def __init__(self, numColorsIn, fadeTimeIn, loopTimeIn, brightLevelIn, blankArray):
        self.numColors = numColorsIn
        self.fadeTime = fadeTimeIn
        self.loopTime = loopTimeIn
        self.brightLevel = brightLevelIn
        self.colors = blankArray

    def setColors(self, colorsIn):
        self.colors = colorsIn

    def getNumColors(self):
        return self.numColors

    def getFadeTime(self):
        return self.fadeTime

    def getLoopTime(self):
        return self.loopTime

    def getBrightLevel(self):
        return self.brightLevel

    def getColors(self):
        return self.colors

#test 3


