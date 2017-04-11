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


    print(("About to start network com"))
    t1 = threading.Thread(target = NetworkComThread, args = (MBsIn, directoryIn,))
    t1.daemon = True
    t1.start()
    print(("network com Thread Created and Started"))

def NetworkComThread(MBsIn, directoryIn):

    networkCom1 = network_com.networkCom(MBsIn, directoryIn)

def runRGBModuleControlBlock(MBIn):


    print(("About to start light module thread"))
    t1 = threading.Thread(target=RGBModuleControlThread, args = (MBIn,))
    t1.daemon = True
    t1.start()
    print(("RGB Thread Created and Started"))

def RGBModuleControlThread(MBIn):
    print ("RGBModuleControlThread() {")
    lightsControlBlock = RGB_moduleControlBlock.moduleControlBlock(MBIn)
    print("} RGBModuleControlThread()")

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

if __name__ == "__main__":

    # child processes should ignore /ALL/ signals
    default_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal.SIG_IGN)


    default_handler2 = signal.getsignal(signal.SIGTERM)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
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

    time.sleep(2)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_term_handler)

    while True:

        time.sleep(1)
