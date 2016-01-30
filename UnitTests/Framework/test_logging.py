#!/usr/bin/python

import unittest
from Framework import logging
from Framework import config

class TestLogging(unittest.TestCase):
    def testConfig(self):
        logging.rgb_log(0, "TEST1")   

def main():
    unittest.main()

if __name__ == '__main__':
    main()
