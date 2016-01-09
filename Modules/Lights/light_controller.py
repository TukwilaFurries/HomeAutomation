#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import termios
import tty
import pigpio
import time
import signal 
from decimal import *
from light_model import *
import threading
from light_utils import *

# TODO:
#   Exception Handling
#   Logging (NoLog, Status Messages, Debugging Messages, Full Trace)
#
#

class PiLights:
    RED_PIN   = 17
    GREEN_PIN = 22
    BLUE_PIN  = 24
    RED = 0
    GREEN = 1
    BLUE = 2

    def lockMainLoop(self):
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Locking main loop")
        self.mainLoopLock = True

    def unlockMainLoop(self):
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Unlocking main loop")
        self.mainLoopLock = False

    def setFadeTime(self, ft):
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Fade Time Changed to " + str(ft))
        self.mainLoopLock = True      
        self.fadeTime = ft
        self.mainLoopLock = False

    def setLoopTime(self, lt):
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Loop Time Changed to " + str(lt))
        self.mainLoopLock = True
        self.loopTime = lt
        self.mainLoopLock = False

    def setBrightLevel(self, bl):
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Brightness Chanes to " + str(bl))
        self.mainLoopLock = True       
        self.brightLevel = bl
        self.mainLoopLock = False

    def setColorPattern(self, cp):
        # XXX TODO: Describe the color patterns in detail
        LIGHT_LOG(self.debug_level, LOG_STATUS, "colorPattern: " + self.cp)
        self.mainLoopLock = True
        self.colorPattern = cp
        self.mainLoopLock = False

    def setPattern(self, p):
        # XXX: Describe VERBOSE pattern better
        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "setPattern()") 
        self.mainLoopLock = True
        self.fadeTime = p.getFadeTime()
        self.loopTime = p.getLoopTime()
        self.brightLevel = p.getBrightLevel()
        self.colorPattern = p.getColors()

        LIGHT_LOG(self.debug_level, LOG_STATUS, "Fade Time Changes to " + str(self.fadeTime))
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Loop Time Changed to " + str(self.loopTime))
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Brightnes Changed to " + str(self.brightLevel))
        LIGHT_LOG(self.debug_level, LOG_STATUS, "Pattern changed to " + str(self.colorPattern))
        self.mainLoopLock = False

    def killProgram(self):
        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "killProgram()")
        self.kill = True
        self.mainLoopThread.join()
        self.pi.stop()

    def updateColor(self, color, step):
        color += step
        if color > 255:
            return 255
        if color < 0:
            return 0
        return color

    def setLights(self, pin, brightness, bright):
        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "Setting Pin " + str(pin) + " = " + str(brightness))
        brightness = self.updateColor(brightness, 0)
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        self.pi.set_PWM_dutycycle(pin, realBrightness)

    # fadeTime = The total time to move from one color to the next
    # loopTime = The total time to move through the entire pattern list
    # brightLevel = The total brightness to use
    # pattern = The array of patterns to transition between
    def mainLoop(self):
        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "mainLoop()")
        while (self.kill == False):
            LIGHT_LOG(self.debug_level, LOG_STATUS, "Pattern = " + str(self.colorPattern))

            while (self.mainLoopLock):
                time.sleep(.1)

            for x in range (0, len(self.colorPattern)):
                currentR = self.colorPattern[x][self.RED]
                currentG = self.colorPattern[x][self.GREEN]
                currentB = self.colorPattern[x][self.BLUE]
                self.setLights(self.RED_PIN, currentR, self.brightLevel)           
                self.setLights(self.GREEN_PIN, currentG, self.brightLevel)
                self.setLights(self.BLUE_PIN, currentB, self.brightLevel)            

                if (x == (len(self.colorPattern)-1)):
                    futureR = self.colorPattern[0][self.RED]
                    futureG = self.colorPattern[0][self.GREEN]
                    futureB = self.colorPattern[0][self.BLUE]
                else:
                    futureR = self.colorPattern[x+1][self.RED]
                    futureG = self.colorPattern[x+1][self.GREEN]
                    futureB = self.colorPattern[x+1][self.BLUE]
               
                rDone = gDone = bDone = False

                while True:
                    # current (positive direction) future
                    
                    if (((self.colorPattern[x][self.RED] <= futureR) and (currentR >= futureR)) or 
                        ((self.colorPattern[x][self.RED] >= futureR) and (currentR <= futureR))):
                        rDone = True
                    
                    if (((self.colorPattern[x][self.GREEN] <= futureG) and (currentG >= futureG)) or 
                        ((self.colorPattern[x][self.GREEN] >= futureG) and (currentG <= futureG))):
                        gDone = True
                    
                    if (((self.colorPattern[x][self.BLUE] <= futureB) and (currentB >= futureB)) or 
                        ((self.colorPattern[x][self.BLUE] >= futureB) and (currentB <= futureB))):
                        bDone = True

                    if (rDone and bDone and gDone):
                        print "All lights transitioned"
                        break

                    if (not rDone):
                        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "rDone is not good")
                        currentR = self.updateColor(currentR, ((futureR - self.colorPattern[x][self.RED]) / self.fadeTime))
                    if (not gDone):
                        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "gDone is not good")
                        currentG = self.updateColor(currentG, ((futureG - self.colorPattern[x][self.GREEN]) / self.fadeTime))
                    if (not bDone):
                        LIGHT_LOG(self.debug_level, LOG_VERBOSE, "bDone is not good")
                        currentB = self.updateColor(currentB, ((futureB - self.colorPattern[x][self.BLUE]) / self.fadeTime))
                    
                    time.sleep(.1)
                    self.setLights(self.RED_PIN, currentR, self.brightLevel)           
                    self.setLights(self.GREEN_PIN, currentG, self.brightLevel)
                    self.setLights(self.BLUE_PIN, currentB, self.brightLevel) 
          
                if (self.loopTime > self.fadeTime):
                    time.sleep((self.loopTime - self.fadeTime) / len(self.colorPattern))
                else:
                    time.sleep ((self.fadeTime - self.loopTime) / len(self.colorPattern))
        self.setLights(self.RED_PIN, 0, 0)
        self.setLights(self.GREEN_PIN, 0, 0)
        self.setLights(self.BLUE_PIN, 0, 0)
        time.sleep(0.1)
        LIGHT_LOG(self.debug_level, LOG_NONE, "Program Terminating")

    def __init__(self):
        self.debug_level = LOG_VERBOSE  
        self.kill = False
        self.fadeTime = 1
        self.loopTime = 1
        self.brightLevel = 1
        self.colorPattern = [] 

        self.pi = pigpio.pi()

        self.mainLoopThread = threading.Thread(target=self.mainLoop)
        self.mainLoopThread.daemon = True
        self.mainLoopThread.start()
        self.mainLoopLock = False

if __name__ == '__main__':
     
    piLights = PiLights()
    try:
        while True:
            for x in range(1, 10):
                piLights.setFadeTime(x)
                piLights.setLoopTime(x)
                time.sleep(.5)
    except KeyboardInterrupt:
        pass

    piLights.killProgram()   
