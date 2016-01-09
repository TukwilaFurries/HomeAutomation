#!/usr/bin/python
import time
import sys

import config

STDOUT = 0
FILE = 1

LIGHT_LOG_OUTPUT = STDOUT

LOG_FILE_IDX = 0
LOG_MODULE_IDX = 1

MODULE_LIST    = [ ["/Log/light.txt", "LIGHT"] ]
LIGHT_LOG_FILE = "./Log/light.txt"
LIGHTS_MODULE = "LIGHTS"

LOG_NONE = 0    # No messages printed
LOG_STATUS= 1   # Status changes
LOG_DEBUG = 2   # Logic decisions, status changes
LOG_VERBOSE = 3 # Code branches, logic decisions, status changes


def LIGHT_LOG_STDOUT(currentLevel, level, message):
    if currentLevel >= level:
        print get_log_stamp("LIGHTS") + message

def LIGHT_LOG_FILE(currentLevel, level, message):
    if currentLevel >= level:
        f1 = open(LIGHT_LOG_FILE, 'w+')
        f1.write(format_message(message, LIGHTS))

# XXX TODO: Some mode to print to screen AND file
def LIGHT_LOG(currentLevel, level, message):
    if LIGHT_LOG_OUTPUT == STDOUT:
        LIGHT_LOG_STDOUT(currentLevel, level, message)
    if LIGHT_LOG_OUTPUT == FILE:
        LIGHT_LOG_FILE(currentLevel, level, message)

def LOG_STDOUT(message, module):
    print get_log_stamp(module) + message

def LOG_FILE(message, module, filename):
    f1 = open(filename, 'w+')
    f1.write(get_log_stamp(module) + message)


def get_log_stamp(module):
    return (time.strftime("%d/%m/%Y %H:%M:%S") + " [" + module + "] ")

# This is the thing that does the meat of the work. Everything else is
# just a fancy wrapper for this, and all the arguments and logic it does

# module - the module that called this
# curLogLvl - The current log level
# conLogLvl - The configured level for this statement to log under
# output - Where this log message is going
#   1 - STDOUT
#   2 - module's defined log file
#   3 - STDOUT and module's defined log file
# message - The message to br printed
#def LOG(module, curLogLlvl, conLogLvl, output, message):
#    if (curLogLvl >= conLogLvl):

if __name__=='__main__':
    print "HI"
    #LIGHT_LOG_STDOUT(2,2,"STDOUT Message")
    #LIGHT_LOG_FILE(2, 2, "FILE Message")
