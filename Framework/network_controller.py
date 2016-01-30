#!/usr/bin/python

# TODO: 1)create array to store various different sockets to monitor different ports, or to keep track of threads monitoring those ports
# This program runs on the pi and receives messages from the network

import socket

from Modules.RGB import module_control_block as RGB_moduleControlBlock
import threading

#initial greeting
def initial_greeting():

    print ''
    print ''
    print '******************************************************************'
    print 'This Program runs on the Pi and receives communication from the linux server'
    print ''
    print ''

initial_greeting()

lightsControlBlock = RGB_moduleControlBlock.moduleControlBlock()
