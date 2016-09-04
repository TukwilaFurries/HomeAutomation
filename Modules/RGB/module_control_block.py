#!/usr/bin/python3

import threading
from light_model import Pattern
import time
from light_controller import *
import struct
#import logging as log

import multiprocessing as mp
from multiprocessing.managers import BaseManager

# 1 digit, control char - 0 is command to gracefully shutdown
# 3 digits, numColors - number of colors
# 9 digits, fadeTime - fade time
# 9 digits, loopTime - total loop time
# 3 digits, brightLevel - intensity/brightness
# 25 total


class moduleControlBlock:

    #takes in a string representing the parameters for a pattern, and creates and returns a pattern object with those parameters
    def parseParameters(self, msgIn):

#        log.rgb_log(log.LEVEL.VERBOSE, "Light Module parsing message into parameters")

        control = struct.unpack_from('I', msgIn, offset=0)


        if(int(control[0]) == 1):
#            log.rgb_log(log.LEVEL.DEBUG, "Light Module received graceful shutdown command")

            self.shutDown = True
            return 1

        numColors = struct.unpack_from('I', msgIn, offset=4)[0]
        fadeTime = struct.unpack_from('I', msgIn, offset=8)[0]
        loopTime = struct.unpack_from('I', msgIn, offset=12)[0]
        brightLevel = struct.unpack_from('I', msgIn, offset=16)[0]
        patternParameters = []
#        log.rgb_log(log.LEVEL.VERBOSE, "params are "+ str(control) + " " + str(numColors) + " " + str(fadeTime) + " " + str(loopTime) + " " + str(brightLevel))
        colors = [999,999,999]
        colors = self.parseColors(msgIn, numColors)

        return Pattern(numColors, fadeTime, loopTime, brightLevel, colors)

    #takes in a string (RRRGGGBBB) and parses the colors into an array of ints
    def parseColors(self, msgIn, numColors):
#        log.rgb_log(log.LEVEL.VERBOSE, "Light Module parsing colors into pattern")
        toReturn = []
        msgOffset = 20
        for x in range (0, numColors):
            rInt = struct.unpack_from('I', msgIn, msgOffset)[0]
            msgOffset += 4
            gInt = struct.unpack_from('I', msgIn, msgOffset)[0]
            msgOffset += 4
            bInt = struct.unpack_from('I', msgIn, msgOffset)[0]
            msgOffset += 4
            toReturn.append([rInt, gInt, bInt])
            print ('colors to add is: ', toReturn)
        return toReturn

    
    def runController(self):

        from light_controller import PiLights

        class MyPiLightsManager(BaseManager): pass

        mp.set_start_method('spawn')
       
        MyPiLightsManager.register('PiLights', PiLights)
        manager = MyPiLightsManager()
        manager.start()

        self.piLights = manager.PiLights()
        process = mp.Process(target=mainLoop, args=(piClass,), name="PiLights")




#        log.rgb_log(log.LEVEL.VERBOSE, "pilights established")


    def __init__(self, mailBoxIn):


        self.shutDown = 0;
#        log.rgb_log(log.LEVEL.DEBUG, "Light Module initializing, starting controller and listening for messages")


        del mailBoxIn[:]

        self.shutDown = False
        self.runController()        

        while(not self.shutDown):
            time.sleep(3)
            if(len(mailBoxIn)>0):

#                log.rgb_log(log.LEVEL.VERBOSE, "Light module has found a new message in its mailbox")
                toParse = mailBoxIn.pop()
                response = self.parseParameters(toParse)

                if (response == 1):
                    log.rgb_log(log.LEVEL.DEBUG, "Light Module ShutDown flag is true, control block sending shutdown command to pilights")
                    self.piLights.killProgram()
                    time.sleep(8)
                    self.shutDown = True

                else:
                    self.piLights.setPattern(response)

