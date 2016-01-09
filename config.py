#!/usr/bin/python

import os

# Directory path variables
DIR_BASE = os.path.dirname(os.path.realpath(__file__))
DIR_FRAMEWORK   = DIR_BASE + "/Framework"
DIR_LOGS        = DIR_BASE + "/Logs"
DIR_MODULES     = DIR_BASE + "/Modules"

PI_ADDRESS     = "10.0.0.98"
SERVER_ADDRESS = "10.0.0.99" 



if __name__ == "__main__":
    print DIR_BASE
    print DIR_FRAMEWORK
    print DIR_LOGS
    print DIR_MODULES

