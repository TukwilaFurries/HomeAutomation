#!/usr/bin/python
# -*- coding: utf-8 -*-
from light_controller import *
from light_model import *
from light_utils import *
import time
if __name__ == '__main__':
    numColors = 3
    fade = 20
    loop = 20
    bright = 255
    colors1 = [[255, 0,0 ], [0, 255,0], [0,0,255]]
    colors2 = [[64, 128, 255], [255,128,64], [128,255,64]]

    pattern1 = Pattern(len(colors1), fade, loop, bright, colors1)
    pattern2 = Pattern(len(colors2), fade, loop, bright, colors2)

    LIGHT_LOG(0, 0, "Synchronizing Lights")
    piLights = PiLights()

    LIGHT_LOG(0, 0, "Phase 1")

    LIGHT_LOG(0, 0, "Phase 2")
    piLights.setPattern(pattern1)
    time.sleep(60)

    LIGHT_LOG(0, 0, "Phase 3")
    piLights.setPattern(pattern2)
    time.sleep(60)

    LIGHT_LOG(0, 0, "Kill All Childre")
    piLights.killProgram()
