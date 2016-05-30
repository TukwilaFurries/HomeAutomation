#This object listens for incoming messages on the lights socket and hands that message off

# Definition of string transmitted by the linux server
# 1 digit, terminateChar - terminate session character, (default value "9" indicates session still open)
# 3 digits, numColors - number of colors
# 9 digits, fadeTime - fade time
# 9 digits, loopTime - total loop time
# 3 digits, brightLevel - intensity/brightness
# 25 total
# (numColors*9) digits - 9-digit RGB values for each color of the pattern

import socket

from light_model import Pattern
from Framework import logging as log

class lightsListener:

    

    #parse the provided string into individual parameters
    def parse_parameters(self, firstMessage):

        terminateChar = int(firstMessage[0])
        numColors = int("" + firstMessage[1] + firstMessage[2] +firstMessage[3])
        fadeTime = int("" + firstMessage[4] + firstMessage[5] + firstMessage[6] + firstMessage[7] + firstMessage[8] + firstMessage[9] + firstMessage[10] + firstMessage[11] + firstMessage[12])
        loopTime = int("" + firstMessage[13] + firstMessage[14] + firstMessage[15] + firstMessage[16] + firstMessage[17] + firstMessage[18] + firstMessage[19] + firstMessage[20] + firstMessage[21])
        brightLevel = int("" + firstMessage[22] + firstMessage[23] + firstMessage[24])
        patternParameters = []
        colors = [999,999,999]

        return Pattern(numColors, fadeTime, loopTime, brightLevel, colors)

    #parse the colors into a nested array ( array of array of ints )
    def parseColors(self, secondMessage, numColors):
        toReturn = []
        for x in range (0, numColors):
            rString = int("" + secondMessage[((9 *x))] + secondMessage[((9 *x)+1)] + secondMessage[((9 *x)+2)])
    #        print "rstring is: "
    #        print rString
            gString = int("" + secondMessage[((9 *x)+3)] + secondMessage[((9 *x)+4)] + secondMessage[((9 *x)+5)])
    #        print "gstring is: "
    #        print gString
            bString = int("" + secondMessage[((9 *x)+6)] + secondMessage[((9 *x)+7)] + secondMessage[((9 *x)+8)])
    #        print "bstring is: "
    #        print bString
            toReturn.append([rString, gString, bString])
        return toReturn

    def __init__(self):
        log.rgb_log(log.LEVEL.VERBOSE, "Light listener activated")


        
    def recMsg(self, queueIn, msgIn):

    	# **********************************************************************************************
        # MAIN EXECUTION
        # **********************************************************************************************

        # Called by the network controllers com thread by callback, this function takes an incoming message and parses it for the RGB module


        pattern1 = Pattern(1,1,1,1,[999,999,999])
        pattern1 = self.parse_parameters(msgIn)
        
        print "numcolors is: " 
        print pattern1.getNumColors()
        print "fadeTime is: " 
        print pattern1.getFadeTime()
        print "loopTime is: " 
        print pattern1.getLoopTime()
        print "brightLevel is: " 
        print pattern1.getBrightLevel()
        print ""
        
    
        print ''
        print 'colors are:'
        print pattern1.getColors()
        print ''
        
        recv2 = msgIn[25:]
        print 'recv2 is:'
        print recv2
    
        pattern1.setColors(self.parseColors(recv2, pattern1.getNumColors()))
        
        print ''
        print 'colors are:'
        print pattern1.getColors()
        print ''
        queueIn.append(pattern1)

        return True
    

    


