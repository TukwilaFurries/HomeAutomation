#!/usr/bin/python

import lights_listener
import module_com
import threading
from light_model import Pattern
import time
from light_controller import *
from lights_listener import *

class moduleControlBlock:
    patternQueue = []
    shutDown = False
    piLightsDone = False
    comCallBack = 0

    def runListener(self):  
        log.rgb_log(log.LEVEL.VERBOSE, "Light Module listener thread initializing")
        lightsListener1 = lights_listener.lightsListener()
        self.shutDown = lightsListener1.runListener(self.patternQueue)
        return

    def runCom(self):
        log.rgb_log(log.LEVEL.VERBOSE, "Light Module com thread initializing")
        lightsListener1 = lights_listener.lightsListener()
        self.shutDown = lightsListener1.runListener(self.patternQueue)
        return

    def getComCallBack(self):
        return comCallBack
        
    
    def runController(self):
        log.rgb_log(log.LEVEL.VERBOSE, "Light Module controller thread initializing")
        from light_controller import PiLights
        piLights = PiLights()
        log.rgb_log(log.LEVEL.VERBOSE, "pilights established")
        
        while True:
            if self.shutDown:
                piLights.killProgram()
                time.sleep(1)
                self.piLightsDone = True
                return


            log.rgb_log(log.LEVEL.VERBOSE, "Light Module Shutdown is False")


            time.sleep(1)

            if len(self.patternQueue)<=0:
                time.sleep(1)                

            if len(self.patternQueue)>0:

                piLights.setPattern(self.patternQueue.pop(0))                   
    
                #LIGHT_LOG(0, 0, "Kill All Children")

    def __init__(self):

        log.rgb_log(log.LEVEL.VERBOSE, "Light Module initializing, starting listener and controller")
#        t1 = threading.Thread(target=self.runCom, args = ())
#        t1.daemon = True

    
        t2 = threading.Thread(target=self.runController, args = ())
        t2.daemon = True
#        t1.start()
#        t2.start()
        log.rgb_log(log.LEVEL.DEBUG, "Light Module Fully Started")        
        
        moduleCom1 = module_com.module_com()
        comCallBack = moduleCom1.runComRec
        while True:
            if self.shutDown and self.piLightsDone:
                log.rgb_log(log.LEVEL.DEBUG, "Shutting Down Module")
                return
                
            time.sleep(3)
    

    
