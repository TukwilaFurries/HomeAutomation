#!/usr/bin/python3

import socket

#import logging as log
import network_com
from Modules.RGB import module_control_block as RGB_moduleControlBlock
import threading
import time
import config
import struct

import signal
import sys

global moduleMailBoxes

class ModuleInfoBlock:
    moduleName = ''
    moduleMailBoxNum = -1
    moduleStats = 'default'
    

def runNetworkCom(MBsIn, directoryIn):


#    log.framework_log(log.LEVEL.DEBUG, "About to start network com")
    t1 = threading.Thread(target = NetworkComThread, args = (MBsIn, directoryIn,))
    t1.daemon = True
    t1.start()
#    log.framework_log(log.LEVEL.VERBOSE, "network com Thread Created and Started")

def NetworkComThread(MBsIn, directoryIn):

    networkCom1 = network_com.networkCom(MBsIn, directoryIn)

def runRGBModuleControlBlock(MBIn):


#    log.framework_log(log.LEVEL.DEBUG, "About to start light module thread")
    t1 = threading.Thread(target=RGBModuleControlThread, args = (MBIn,))
    t1.daemon = True
    t1.start()
#    log.framework_log(log.LEVEL.VERBOSE, "RGB Thread Created and Started")

def RGBModuleControlThread(MBIn):

    lightsControlBlock = RGB_moduleControlBlock.moduleControlBlock(MBIn)

def signal_term_handler(signal, frame):
    print ('got SIGTERM')
    endSignal = struct.pack('I', 1)
    moduleMailBoxes[1].append(endSignal)
    time.sleep(5)
    sys.exit(0)

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print ('got SIGINT')
    endSignal = struct.pack('I', 1)
    moduleMailBoxes[1].append(endSignal)
    time.sleep(5)
    sys.exit(0)

print ('running new network controller')


moduleMailBoxes = []

moduleInfoBlocks = []

MB0 = []
MB1 = []

moduleMailBoxes.append(MB0)
moduleMailBoxes.append(MB1)

mailboxDirectory = {config.MODULES.NETWORK_CONTROLLER.ID:moduleMailBoxes[0], config.MODULES.RGB.ID:moduleMailBoxes[1]}



runRGBModuleControlBlock(MB1)

runNetworkCom(moduleMailBoxes, mailboxDirectory)



while True:


    signal.signal(signal.SIGINT, signal_handler)
 
    signal.signal(signal.SIGTERM, signal_term_handler)

    time.sleep(1)
