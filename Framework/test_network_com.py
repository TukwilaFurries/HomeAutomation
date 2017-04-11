import unittest
import socket
import time

import network_com

class NetworkComTest(unittest.TestCase):

    def test_create_network_com(self):
        testMailBoxes = []
        testDirectory = {}
        networkCom1 = network_com.networkCom(testMailBoxes, testDirectory)
        print ('here')
        lightControlSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        lightControlSocket.connect(('10.0.0.98', 15555))
        
