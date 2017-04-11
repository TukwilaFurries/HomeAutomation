#!/usr/bin/python3

import pigpio
import signal 
from decimal import *
from multiprocessing.managers import BaseManager
from Modules.RGB.light_model import *
import pi_config
from time import sleep
from Framework.home_automation_logging import HomeAutomationLogging

from Modules.RGB.light_controller import *
import multiprocessing as mp

class MyPiLightsManager(BaseManager): pass

if True:
    print("Go")
    MyPiLightsManager.register('PiLights', PiLights)
    manager = MyPiLightsManager()

    # child processes should ignore /ALL/ signals
    default_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    
    # Start everything up
    manager.start()
    piClass = manager.PiLights()
    process = mp.Process(target=mainLoop, args=(piClass,), name="PiLights")
    process.start()

    signal.signal(signal.SIGINT, default_handler)

    numColors = 3
    fadeTime = 3 
    loopTime = 1 
    brightLevel = 128 
    A=85
    B=170
    C=255
    colors = [ [A,B,C], [B,C,A], [C,A,B]]
    pattern = Pattern(numColors, fadeTime, loopTime, brightLevel, colors)

    piClass.setPattern(pattern)
    try:
        while(True):
            sleep(.01)
    except KeyboardInterrupt:
        piClass.killProgram()
        process.join()
