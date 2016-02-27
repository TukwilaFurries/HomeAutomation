#!/usr/bin/python

import unittest
from Modules.RGB import module_control_block

import time

class  test_light_control(unittest.TestCase):
    def test(self):
        mcb = module_control_block.moduleControlBlock()

if __name__ == '__main__':
    unittest.main()
