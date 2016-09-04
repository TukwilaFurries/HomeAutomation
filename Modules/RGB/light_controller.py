#!/usr/bin/python3
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
import multiprocessing as mp
from multiprocessing.managers import BaseManager
from light_model import *
import pi_config
from time import sleep
import setproctitle
import home_automation_logging
from home_automation_logging import HomeAutomationLogging
# TODO:
#   Exception Handling
#   Logging (NoLog, Status Messages, Debugging Messages, Full Trace)
#
#

class PiLights:

    def getMainLoopLock(self):
        return self.mainLoopLock

    def lockMainLoop(self):
        self.log.debug("lockMainLoop()")
        self.mainLoopLock = True

    def unlockMainLoop(self):
        self.log.debug("unlockMainLoop()")
        self.mainLoopLock = False

    def setFadeTime(self, ft):
        self.log.info("Fade Time Changed to " + str(ft))
        self.mainLoopLock = True      
        self.fadeTime = ft
        self.mainLoopLock = False
        self.configChagned = True
    def getFadeTime(self):
        return self.fadeTime

    def setLoopTime(self, lt):
        self.log.info("Loop Time Changed to " + str(lt))
        self.mainLoopLock = True
        self.loopTime = lt
        self.mainLoopLock = False
        self.configChanged = True
    def getLoopTime(self):
        return self.loopTime

    def setBrightLevel(self, bl):
        self.log.info("Brightness Chanes to " + str(bl))
        self.mainLoopLock = True       
        self.brightLevel = bl
        self.mainLoopLock = False
        self.configChanged = True
    def getBrightLevel(self):
        return self.brightLevel

    def setColorPattern(self, cp):
        self.log.info("Color Pattern changed to: " + self.cp)
        self.mainLoopLock = True
        self.colorPattern = cp
        self.numColors = len(cp)
        self.mainLoopLock = False
        self.configChanged = True
    def getColorPattern(self):
        return self.colorPattern

    def setPattern(self, p):
        self.log.debug("setPattern()") 
        self.mainLoopLock = True
        self.setFadeTime(p.getFadeTime())
        self.setLoopTime(p.getLoopTime())
        self.setBrightLevel(p.getBrightLevel())
        self.setColorPattern(p.getColors())
        self.setNumColors(p.getNumColors)
        self.lockMainLoop()
        self.setConfigChanged(True)

    def killProgram(self):
        self.log.info("Kill Program Recieved")
        self.kill = True
        self.configChanged = True
        #self.mainLoopThread.join()
        self.pi.stop()

    def continue_loop(self):
        return not self.kill
    
    def updateColor(self, color, step):
        color += step
        if color > 255:
            return 255
        if color < 0:
            return 0
        return color

    def setLights(self, pin, brightness, bright):
        self.log.debug("Setting Pin " + str(pin) + " = " + str(brightness))
        brightness = self.updateColor(brightness, 0)
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        self.pi.set_PWM_dutycycle(pin, realBrightness)

    def getNumColors(self):
        return self.numColors

    def setConfigChanged(self, changed):
        self.configChanged = changed

    def getConfigChanged(self):
        return self.configChanged

    def __init__(self):
        self.kill = False
        self.fadeTime = 1
        self.loopTime = 1
        self.brightLevel = 1
        self.colorPattern = [] 
        self.numColors = 0
        self.pi = pigpio.pi()
        self.mainLoopLock = False
        self.configChanged = False
        self.log = HomeAutomationLogging(pi_config.RGB.getLogLocation())

# fadeTime = The total time to move from one color to the next
# loopTime = The total time to move through the entire pattern list
# brightLevel = The total brightness to use
# pattern = The array of patterns to transition between
def mainLoop(pi_lights):
    setproctitle.setproctitle("LightController")
    self.log.debug("mainLoop()")
    while (pi_lights.continue_loop() == True):
        pi_lights.setConfigChanged(False)

        while (pi_lights.getMainLoopLock()):
            print("Main Loop Locked")
            #log.rgb_log(log.LEVEL.DEBUG, "Main Loop Locked")
            time.sleep(.1)

        for x in range (0, pi_lights.getNumColors()):
            print("Iteration: %u of %u" % (x, pi_lights.getNumColors()))
            if pi_lights.getConfigChanged():
                print("Configuration Changed")
                break

            currentR = pi_lights.getColorPattern()[x][RGB.SPECTRUM.R]
            currentG = pi_lights.getColorPattern()[x][RGB.SPECTRUM.G]
            currentB = pi_lights.getColorPattern()[x][RGB.SPECTRUM.B]
            pi_lights.setLights(pi_config.RGB.getPinR(), currentR, pi_lights.getBrightLevel())           
            pi_lights.setLights(pi_config.RGB.getPinG(), currentG, pi_lights.getBrightLevel())
            pi_lights.setLights(pi_config.RGB.getPinB(), currentB, pi_lights.getBrightLevel())            
            print("X: %u / %u" % (x, pi_lights.getNumColors()))
            if (x == pi_lights.getNumColors()-1):
                futureR = pi_lights.getColorPattern()[0][RGB.SPECTRUM.R]
                futureG = pi_lights.getColorPattern()[0][RGB.SPECTRUM.G]
                futureB = pi_lights.getColorPattern()[0][RGB.SPECTRUM.B]
            else:
                futureR = pi_lights.getColorPattern()[x+1][RGB.SPECTRUM.R]
                futureG = pi_lights.getColorPattern()[x+1][RGB.SPECTRUM.G]
                futureB = pi_lights.getColorPattern()[x+1][RGB.SPECTRUM.B]
               
            rDone = gDone = bDone = False

            while True:
                if pi_lights.getConfigChanged():
                    break
                # current (positive direction) future
                  
                if (((pi_lights.getColorPattern()[x][RGB.SPECTRUM.R] <= futureR) and (currentR >= futureR)) or 
                    ((pi_lights.getColorPattern()[x][RGB.SPECTRUM.R] >= futureR) and (currentR <= futureR))):
                    rDone = True
                    
                if (((pi_lights.getColorPattern()[x][RGB.SPECTRUM.G] <= futureG) and (currentG >= futureG)) or 
                    ((pi_lights.getColorPattern()[x][RGB.SPECTRUM.G] >= futureG) and (currentG <= futureG))):
                    gDone = True
                    
                if (((pi_lights.getColorPattern()[x][RGB.SPECTRUM.B] <= futureB) and (currentB >= futureB)) or 
                    ((pi_lights.getColorPattern()[x][RGB.SPECTRUM.B] >= futureB) and (currentB <= futureB))):
                    bDone = True

                if (rDone and bDone and gDone):
                    #log.rgb_log(log.LEVEL.VERBOSE, "All lights transitioned")
                    break

                if (not rDone):
                    #log.rgb_log(log.LEVEL.VERBOSE, "rDone is not good")
                    currentR = pi_lights.updateColor(currentR, ((futureR - pi_lights.getColorPattern()[x][0]) / pi_lights.getFadeTime()))
                if (not gDone):
                    #log.rgb_log(log.LEVEL.VERBOSE, "gDone is not good")
                    currentG = pi_lights.updateColor(currentG, ((futureG - pi_lights.getColorPattern()[x][1]) / pi_lights.getFadeTime()))
                if (not bDone):
                    #log.rgb_log(log.LEVEL.VERBOSE, "bDone is not good")
                    currentB = pi_lights.updateColor(currentB, ((futureB - pi_lights.getColorPattern()[x][2]) / pi_lights.getFadeTime()))
                    
                time.sleep(.1)
                pi_lights.setLights(pi_config.RGB.getPinR(), currentR, pi_lights.getBrightLevel())           
                pi_lights.setLights(pi_config.RGB.getPinG(), currentG, pi_lights.getBrightLevel())
                pi_lights.setLights(pi_config.RGB.getPinB(), currentB, pi_lights.getBrightLevel()) 
          
            if (pi_lights.getLoopTime() > pi_lights.getFadeTime()):
                time.sleep((pi_lights.getLoopTime() - pi_lights.getFadeTime()) / pi_lights.getNumColors())
            else:
                time.sleep ((pi_lights.getFadeTime() - pi_lights.getLoopTime()) / pi_lights.getNumColors())
    pi_lights.setLights(pi_config.RGB.getPinR(), 0, 0)
    pi_lights.setLights(pi_config.RGB.getPinG(), 0, 0)
    pi_lights.setLights(pi_config.RGB.getPinB(), 0, 0)
    time.sleep(0.1)
    #log.rgb_log(log.LEVEL.STATUS, "Program Terminating")


class MyPiLightsManager(BaseManager): pass

if __name__ == '__main__':
    if True:
        print("Go")
        mp.set_start_method('spawn')
        qIn = mp.Queue()
        qOut = mp.Queue()

        print("Creating Multiprocess Class")
        MyPiLightsManager.register('PiLights', PiLights)
        manager = MyPiLightsManager()
        manager.start()

        piClass = manager.PiLights()
        process = mp.Process(target=mainLoop, args=(piClass,), name="PiLights")
        print("Creating Pattern")
        numColors = 3
        fadeTime = 3 
        loopTime = 1 
        brightLevel = 128 
        A=85
        B=170
        C=255
        colors = [ [A,B,C], [B,C,A], [C,A,B]]
        pattern = Pattern(numColors, fadeTime, loopTime, brightLevel, colors)

        print("Beginning Program Now")
        process.start()
        print("Setting Pattern")
        piClass.setPattern(pattern)
        while True:
            try:
                sleep(1)
            except KeyboardInterrupt:
                print("Quitting")
                piClass.killProgram()
                break
