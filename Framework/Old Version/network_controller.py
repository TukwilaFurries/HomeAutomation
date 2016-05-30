#!/usr/bin/python

# TODO: 1)create array to store various different sockets to monitor different ports, or to keep track of threads monitoring those ports
# This program runs on the pi and receives messages from the network

import socket

import logging as log
import network_com
from Modules.RGB import module_control_block as RGB_moduleControlBlock
import threading
import time

#initial greeting
log.rgb_log(log.LEVEL.STATUS, "Network Controller Initiated")





def initial_greeting():

    print ''
    print ''
    print '******************************************************************'
    print 'This Program runs on the Pi and initiates specific Module Control Blocks'
    print ''
    print ''

def runRGBModuleControlBlock():

    log.rgb_log(log.LEVEL.VERBOSE, "About to start light module thread")

    t1 = threading.Thread(target=RGBModuleControlThread, args = ())
    t1.daemon = True
    t1.start()
    log.rgb_log(log.LEVEL.VERBOSE, "Light Module Thread Created and Started")


def RGBModuleControlThread():

    lightsControlBlock = RGB_moduleControlBlock.moduleControlBlock()




networkCom1 = network_com.networkCom()




initial_greeting()
runRGBModuleControlBlock()

networkCom1.runCom(testcb1)

while True:
    log.rgb_log(log.LEVEL.VERBOSE, "NetworkController Main Loop Running")
    time.sleep(10)

    


