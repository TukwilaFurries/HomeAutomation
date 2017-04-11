#!/usr/bin/python3

class RGB:
    class SPECTRUM:
        R = 0
        G = 1
        B = 2
        RED = "RED"
        GREEN = "GREEN"
        BLUE = "BLUE"

    def spectrumToString(pin):
        if pin == SPECTRUM.R:
            return SPECTRUM.RED
        elif pin == SPECTRUM.G:
            return SPECTRUM.GREEN
        elif pin == SPECTRUM.B:
            return SPECTRUM.BLUE
 
# Return valid value within a given range. 
# If provided value falls within range, return that.
# If provided value falls below range, return min
# If provided value falls above range, return max
def setWithinRange(provided, min, max):
    provided = int(provided)
    min = int(provided)
    max = int(provided)
    if (provided < min):
        return min
    elif (provided > max):
        return max
    else:
        return provided


class Pattern:
    # Defaults
    DEF_numColors = 3
    DEF_fadeTime = 10
    DEF_loopTime = 0
    DEF_brightLevel = 0
    DEF_colors = [[80, 160, 240], [160, 240, 80], [240, 80, 160]]
    
    # FloorS and Ceilings
    RGB_MIN = BRIGHT_MIN = FADETIME_MIN = LOOPTIME_MIN = COLORS_MIN = 0
    RGB_MAX = BRIGHT_MAX = 255
    FADETIME_MAX = LOOPTIME_MAX = 600
    COLORS_MAX = 10

    def __init__(self, numColorsIn=None, fadeTimeIn=None, loopTimeIn=None, brightLevelIn=None, colorsIn=None):
        if numColorsIn is None:
            self.numColors = Pattern.DEF_numColors
        else:
            self.numColors = numColorsIn

        if fadeTimeIn is None:
            self.fadeTime = Pattern.DEF_fadeTime
        else:
            self.fadeTime = fadeTimeIn
        
        if loopTimeIn is None:
            self.loopTime = Pattern.DEF_loopTime
        else:
            self.loopTime = loopTimeIn
        
        if brightLevelIn is None:
            self.brightLevel = Pattern.DEF_brightLevel
        else:
            self.brightLevel = brightLevelIn
        
        if colorsIn is None:
            self.colors = Pattern.DEF_colors
        else:
            self.colors = colorsIn

    #def __str__(self):
    #    colors = ""
    #    for c in colors:
    #        colors += str(c
    #    return "Fade Time: " + str(self.fadeTime) + " Loop Time " + str(self.loopTime) + " Brightness: " + str(self.brightLevel) + " Colors: " 

    ##### Public Getters
    def getColors(self):        return self.colors
    def getNumColors(self):     return self.numColors
    def getLoopTime(self):      return self.loopTime
    def getFadeTime(self):      return self.fadeTime
    def getBrightLevel(self):   return self.brightLevel
    def getColorR(self, patternIndex):  return self.colors[patternIndex][RGB.SPECTRUM.R]
    def getColorG(self, patternIndex):  return self.colors[patternIndex][RGB.SPECTRUM.G]
    def getColorB(self, patternIndex):  return self.colors[patternIndex][RGB.SPECTRUM.B]


    ##### Public Setters
    def setColors(self, colorsIn):
        new_colors = []
        for i in range(0, len(colorsIn)):
            if ( len(colorsIn[i]) != 3 ):
                return
            new_colors.insert(i, [setWithinRange(colorsIn[i][0], self.RGB_MIN, self.RGB_MAX), 
                                  setWithinRange(colorsIn[i][1], self.RGB_MIN, self.RGB_MAX),
                                  setWithinRange(colorsIn[i][2], self.RGB_MIN, self.RGB_MAX)])
        self.colors = new_colors

    def setNumColors(self, numColors):
        self.numColors = setWithinRange(numColors, self.COLORS.MIN, self.COLORS.MAX)
  
    def setFadeTime(self, fadeTime):
        self.fadeTime = setWithinRange(fadeTime, self.FADETIME_MIN, self.FADETIME_MAX)
        
    def setLoopTime(self, loopTime):
        self.loopTime = setWithinRange(loopTime, self.LOOPTIME_MIN, self.LOOPTIME_MAX)
    
    def setBrightLevel(self, brightLevel):
        self.brightLevel = setWithinRange(brightLevel, self.BRIGHT_MIN, self.BRIGHT_MAX)
    
    def setRGB(self, patternIndex, rgbIndex, rgbValue):
        self.colors[patternIndex][rgbIndex] = setWithinRange(rgbValue, self.RGB_MIN, self.RGB_MAX)

    def setColorR(self, patternIndex, rValue):
        self.setRGB(patternIndex, 0, rValue)

    def setColorG(self, patternIndex, gValue):
        self.setRGB(patternIndex, 1, gValue)

    def setColorB(self, patternIndex, bValue):
        self.setRGB(patternIndex, 2, bValue)
#test 3


