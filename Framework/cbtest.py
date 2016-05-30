#!/usr/bin/python

import socket

import logging as log
from Modules.RGB import module_control_block as RGB_moduleControlBlock
import threading
import time
import cbtestObject as cbto
import cblistener as cbl


#initial greeting
print 'running cb test'
cbto1 = cbto.cbtestObject()
cb1 = cbto1.cbPrint
cb1('test message')

print 'creating Listener'
cbl1 = cbl.cbListener()
cbl1.addCB(cb1)