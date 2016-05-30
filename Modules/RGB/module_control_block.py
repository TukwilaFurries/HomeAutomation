#!/usr/bin/python

import threading
from light_model import Pattern
import time
from light_controller import *




class moduleControlBlock:

    def parseParameters(self, firstMessage):

        if(firstMessage[0] == 0):
            return '0'

        self.shutDown = True

        terminateChar = int(firstMessage[0])
        numColors = int("" + firstMessage[1] + firstMessage[2] +firstMessage[3])
        fadeTime = int("" + firstMessage[4] + firstMessage[5] + firstMessage[6] + firstMessage[7] + firstMessage[8] + firstMessage[9] + firstMessage[10] + firstMessage[11] + firstMessage[12])
        loopTime = int("" + firstMessage[13] + firstMessage[14] + firstMessage[15] + firstMessage[16] + firstMessage[17] + firstMessage[18] + firstMessage[19] + firstMessage[20] + firstMessage[21])
        brightLevel = int("" + firstMessage[22] + firstMessage[23] + firstMessage[24])
        patternParameters = []
        colors = [999,999,999]
        colors = self.parseColors(firstMessage[25:], numColors)

        return Pattern(numColors, fadeTime, loopTime, brightLevel, colors)

    #parse the colors into a nested array ( array of array of ints )
    def parseColors(self, secondMessage, numColors):
        toReturn = []
        for x in range (0, numColors):
            rString = int("" + secondMessage[((9 *x))] + secondMessage[((9 *x)+1)] + secondMessage[((9 *x)+2)])
            gString = int("" + secondMessage[((9 *x)+3)] + secondMessage[((9 *x)+4)] + secondMessage[((9 *x)+5)])
            bString = int("" + secondMessage[((9 *x)+6)] + secondMessage[((9 *x)+7)] + secondMessage[((9 *x)+8)])
            toReturn.append([rString, gString, bString])
        return toReturn

    
    def runController(self):
        log.rgb_log(log.LEVEL.VERBOSE, "Light Module controller thread initializing")
        from light_controller import PiLights
        self.piLights = PiLights()
        log.rgb_log(log.LEVEL.VERBOSE, "pilights established")


    def __init__(self, mailBoxIn):


        self.shutDown = 0;
        log.rgb_log(log.LEVEL.VERBOSE, "Light Module initializing, starting listener and controller")
        print 'RGB MCB running'

        time.sleep(2)

        print mailBoxIn
        del mailBoxIn[:]
        time.sleep(10)
        print mailBoxIn

        shutDown = False
        self.runController()

        

        while(not shutDown):
            print 'in while loop'
            time.sleep(2)
            if(len(mailBoxIn)>0):
                print 'mailbox has message: ', mailBoxIn[0]
                response = self.parseParameters(mailBoxIn.pop())
                print response
                self.piLights.setPattern(response)
        else:
            return 1

