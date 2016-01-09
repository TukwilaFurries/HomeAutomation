#!/usr/bin/python

# TODO: 1)create array to store various different sockets to monitor different ports, or to keep track of threads monitoring those ports
# This program runs on the pi and receives messages from the network

import socket
import lights_listener

#initial greeting
def initial_greeting():

    print ''
    print ''
    print '******************************************************************'
    print 'This Program runs on the Pi and receives communication from the linux server'
    print ''
    print ''

initial_greeting()

lightListern1 = lightListener()

print 'Test1234'