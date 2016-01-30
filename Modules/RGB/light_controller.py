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
import threading

from Modules import *
from Framework import *
#from Framework import logging as log
from Modules.RGB.light_model import *
from Framework.config import *
from Modules.RGB.light_model import *

import Framework.config

# TODO:
#   Exception Handling
#   Logging (NoLog, Status Messages, Debugging Messages, Full Trace)
#
#

class PiLights:
    RED_PIN   = 17
    GREEN_PIN = 22
    BLUE_PIN  = 24

    def lockMainLoop(self):
        log.rgb_log(log.LEVEL.VERBOSE, "lockMainLoop()")
        self.mainLoopLock = True

    def unlockMainLoop(self):
        log.rgb_log(log.LEVEL.VERBOSE, "unlockMainLoop()")
        self.mainLoopLock = False

    def setFadeTime(self, ft):
        log.rgb_log(log.LEVEL.STATUS, "Fade Time Changed to " + str(ft))
        self.mainLoopLock = True      
        self.fadeTime = ft
        self.mainLoopLock = False
        self.configChagned = True

    def setLoopTime(self, lt):
        log.rgb_log(log.LEVEL.STATUS, "Loop Time Changed to " + str(lt))
        self.mainLoopLock = True
        self.loopTime = lt
        self.mainLoopLock = False
        self.configChanged = True

    def setBrightLevel(self, bl):
        log.rgb_log(log.LEVEL.STATUS, "Brightness Chanes to " + str(bl))
        self.mainLoopLock = True       
        self.brightLevel = bl
        self.mainLoopLock = False
        self.configChanged = True

    def setColorPattern(self, cp):
        log.rgb_log(log.LEVEL.STATUS, "colorPattern: " + self.cp)
        self.mainLoopLock = True
        self.colorPattern = cp
        self.mainLoopLock = False
        self.configChanged = True

    def setPattern(self, p):
        log.rgb_log(log.LEVEL.VERBOSE, "setPattern()") 
        self.mainLoopLock = True
        self.fadeTime = p.getFadeTime()
        self.loopTime = p.getLoopTime()
        self.brightLevel = p.getBrightLevel()
        self.colorPattern = p.getColors()

        log.rgb_log(log.LEVEL.STATUS, "Fade Time Changed to " + str(self.fadeTime))
        log.rgb_log(log.LEVEL.STATUS, "Loop Time Changed to " + str(self.loopTime))
        log.rgb_log(log.LEVEL.STATUS, "Brightnes Changed to " + str(self.brightLevel))
        log.rgb_log(log.LEVEL.STATUS, "Pattern changed to " + str(self.colorPattern))
        self.mainLoopLock = False
        self.configChanged = True

    def killProgram(self):
        log.rgb_log(log.LEVEL.STATUS, "killProgram()")
        self.kill = True
        self.configChanged = True
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
        #log.rgb_log(log.LEVEL.DEBUG, "Setting Pin " + str(pin) + " = " + str(brightness))
        brightness = self.updateColor(brightness, 0)
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        self.pi.set_PWM_dutycycle(pin, realBrightness)

    # fadeTime = The total time to move from one color to the next
    # loopTime = The total time to move through the entire pattern list
    # brightLevel = The total brightness to use
    # pattern = The array of patterns to transition between
    def mainLoop(self):
        log.rgb_log(log.LEVEL.DEBUG, "mainLoop()")
        while (self.kill == False):
            self.configChanged = False
            while (self.mainLoopLock):
                log.rgb_log(log.LEVEL.DEBUG, "Main Loop Locked")
                time.sleep(.1)
            for x in range (0, len(self.colorPattern)):
                if self.configChanged:
                    break
                currentR = self.colorPattern[x][RGB.SPECTRUM.R]
                currentG = self.colorPattern[x][RGB.SPECTRUM.G]
                currentB = self.colorPattern[x][RGB.SPECTRUM.B]
                self.setLights(self.RED_PIN, currentR, self.brightLevel)           
                self.setLights(self.GREEN_PIN, currentG, self.brightLevel)
                self.setLights(self.BLUE_PIN, currentB, self.brightLevel)            

                if (x == (len(self.colorPattern)-1)):
                    futureR = self.colorPattern[0][RGB.SPECTRUM.R]
                    futureG = self.colorPattern[0][RGB.SPECTRUM.G]
                    futureB = self.colorPattern[0][RGB.SPECTRUM.B]
                else:
                    futureR = self.colorPattern[x+1][RGB.SPECTRUM.R]
                    futureG = self.colorPattern[x+1][RGB.SPECTRUM.G]
                    futureB = self.colorPattern[x+1][RGB.SPECTRUM.B]
               
                rDone = gDone = bDone = False

                while True:
                    if self.configChanged:
                        break
                    # current (positive direction) future
                    
                    if (((self.colorPattern[x][RGB.SPECTRUM.R] <= futureR) and (currentR >= futureR)) or 
                        ((self.colorPattern[x][RGB.SPECTRUM.R] >= futureR) and (currentR <= futureR))):
                        rDone = True
                    
                    if (((self.colorPattern[x][RGB.SPECTRUM.G] <= futureG) and (currentG >= futureG)) or 
                        ((self.colorPattern[x][RGB.SPECTRUM.G] >= futureG) and (currentG <= futureG))):
                        gDone = True
                    
                    if (((self.colorPattern[x][RGB.SPECTRUM.B] <= futureB) and (currentB >= futureB)) or 
                        ((self.colorPattern[x][RGB.SPECTRUM.B] >= futureB) and (currentB <= futureB))):
                        bDone = True

                    if (rDone and bDone and gDone):
                        log.rgb_log(log.LEVEL.VERBOSE, "All lights transitioned")
                        break

                    if (not rDone):
                        log.rgb_log(log.LEVEL.VERBOSE, "rDone is not good")
                        currentR = self.updateColor(currentR, ((futureR - self.colorPattern[x][0]) / self.fadeTime))
                    if (not gDone):
                        log.rgb_log(log.LEVEL.VERBOSE, "gDone is not good")
                        currentG = self.updateColor(currentG, ((futureG - self.colorPattern[x][1]) / self.fadeTime))
                    if (not bDone):
                        log.rgb_log(log.LEVEL.VERBOSE, "bDone is not good")
                        currentB = self.updateColor(currentB, ((futureB - self.colorPattern[x][2]) / self.fadeTime))
                    
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
        log.rgb_log(log.LEVEL.STATUS, "Program Terminating")

    def __init__(self):
        self.kill = False
        self.fadeTime = 1
        self.loopTime = 1
        self.brightLevel = 1
        self.colorPattern = [] 

        self.pi = pigpio.pi()

        self.mainLoopThread = threading.Thread(target=self.mainLoop)
        self.mainLoopThread.daemon = True
        self.mainLoopLock = False      
        self.mainLoopThread.start()

