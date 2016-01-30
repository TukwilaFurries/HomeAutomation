#!/usr/bin/python

import lights_listener
import light_controller
import threading
from light_model import Pattern
import time


class moduleControlBlock:
    patternQueue = []
    shutDown = False
    piLightsDone = False

    def runListener(self):    
        lightsListener1 = lights_listener.lightsListener()
        self.shutDown = lightsListener1.runListener(self.patternQueue)
    
    
    def runController(self):
        
        piLights = light_controller.PiLights()        
        
        while True:
            if self.shutDown:
                piLights.killProgram()
                time.sleep(1)
                self.piLightsDone = True


            print 'shutdown is'
            print self.shutDown

            time.sleep(1)

            if len(self.patternQueue)<=0:
                time.sleep(1)                

            if len(self.patternQueue)>0:

                piLights.setPattern(self.patternQueue.pop(0))                   
    
                #LIGHT_LOG(0, 0, "Kill All Children")

    
    def __init__(self):

        t1 = threading.Thread(target=self.runListener, args = ())
        t1.daemon = True
    
        t2 = threading.Thread(target=self.runController, args = ())
        t2.daemon = True
        t1.start()
        t2.start()
        
        
        print 'entering while true loop'
        while True:
            if self.shutDown and self.piLightsDone:
                return
                
            time.sleep(1)
    

