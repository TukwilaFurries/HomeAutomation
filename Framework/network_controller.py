#!/usr/bin/python

import socket

import logging as log
import network_com
from Modules.RGB import module_control_block as RGB_moduleControlBlock
import threading
import time


class ModuleInfoBlock:
    moduleName = ''
    moduleMailBoxNum = -1
    moduleStats = 'default'
    

def runNetworkCom(MBsIn):


    log.rgb_log(log.LEVEL.VERBOSE, "About to start network com")
    t1 = threading.Thread(target = NetworkComThread, args = (MBsIn,))
    t1.daemon = True
    t1.start()
    log.rgb_log(log.LEVEL.VERBOSE, "network com Thread Created and Started")

def NetworkComThread(MBsIn):

    networkCom1 = network_com.networkCom(MBsIn)

def runRGBModuleControlBlock(MBIn):


    log.rgb_log(log.LEVEL.VERBOSE, "About to start light module thread")
    t1 = threading.Thread(target=RGBModuleControlThread, args = (MBIn,))
    t1.daemon = True
    t1.start()
    log.rgb_log(log.LEVEL.VERBOSE, "Light Module Thread Created and Started")

def RGBModuleControlThread(MBIn):

    lightsControlBlock = RGB_moduleControlBlock.moduleControlBlock(MBIn)

print 'running new network controller'


moduleMailBoxes = []

moduleInfoBlocks = []

MB0 = []
MB1 = []

moduleMailBoxes.append(MB0)
moduleMailBoxes.append(MB1)

runRGBModuleControlBlock(MB1)

runNetworkCom(moduleMailBoxes)

MB1.append('final test')
moduleMailBoxes[1].append('final test 2')


time.sleep(50)
print 'done'