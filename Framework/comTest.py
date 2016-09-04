#!/usr/bin/python
import socket

import config
import logging as log
import network_com
from Modules.RGB import module_control_block as RGB_moduleControlBlock
import threading
import time
import config


def runNetworkCom(MBsIn, directoryIn):


    log.framework_log(log.LEVEL.DEBUG, "About to start network com")
    t1 = threading.Thread(target = NetworkComThread, args = (MBsIn,directoryIn,))
    t1.daemon = True
    t1.start()
    log.framework_log(log.LEVEL.VERBOSE, "network com Thread Created and Started")

def NetworkComThread(MBsIn, directoryIn):

    networkCom1 = network_com.networkCom(MBsIn, directoryIn)


print 'running comTest'


moduleMailBoxes = []

moduleInfoBlocks = []

MB0 = []
MB1 = []



moduleMailBoxes.append(MB0)
moduleMailBoxes.append(MB1)

moduleIDs = {config.MODULES.NETWORK_CONTROLLER.ID:moduleMailBoxes[0], config.MODULES.RGB.ID:moduleMailBoxes[1]}
print 'getClass for ID 0 returns: '
print config.MODULES.getClass(0)

#MB0.append("test1")
#print MB0[0]
#print moduleMailBoxes[0][0]
#print 'dict next'
#print moduleIDs[0][0]



runNetworkCom(moduleMailBoxes, moduleIDs)

while True:
    time.sleep(3)
