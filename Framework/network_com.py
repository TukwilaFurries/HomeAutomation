#!/usr/bin/python3
import socket
import struct
#import logging as log
import time
import select
import config


# The network_com is designed to run in its own thread (it does not start this thread)
# The network_com is launched by the network_controller and handles incoming messages,
#  stripping their (length) and (destination mailbox) bits, and passing the remianing message to that mialbox
# - The initialize method creates a TCP socket and accepts a connection
# - The main loop of execution watches port 15555 on the IP address 10.0.0.98

class networkCom:

    def __init__(self, mailBoxes, directoryIn):

            self.TCP_IP = '10.0.0.98'
            self.TCP_PORT = config.GLOBAL.NETWORK.PIPORT
            self.directory = directoryIn

            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serversocket.bind((self.TCP_IP, self.TCP_PORT))
            self.serversocket.listen(1)
            self.conn, addr = self.serversocket.accept()

#            log.framework_log(log.LEVEL.VERBOSE, "connected to: " +(addr[0]) + ":" + str(addr[1]))
#            log.framework_log(log.LEVEL.VERBOSE, "Com socket established")
            self.runCom(mailBoxes, directoryIn)

    # Receives messages from the network, strips their header (length, desination), determines how much more to receive,
    # what box to send the next message to, receives the next message, and sends that to the box

    def runCom(self, mailBoxesIn, directoryIn):


        #receives the first 8 byte segment:
        # -[0]indicating destination module (32 bits unsigned int)
        # -[1]indicating byte of remaining message to be received (32 bits unsigned int)

        while True:
#            log.framework_log(log.LEVEL.DEBUG, "Network Com awaiting incoming message...")
            time.sleep(.2)

            #for reference, message to be passed to light module
            # 1 character - control character
            # 4 characters - destination module
            # 10 characters - size of remaining message (number of characters)

            data = self.conn.recv(8)
            if not data:
                print ('***************CONNECTION LOST***************')
                break
            data = struct.unpack('II', data)
            destModuleID = data[0]
            toRec = data[1]
#            log.framework_log(log.LEVEL.DEBUG, ('network com received new message (part 1), number of bytes to receive for payload is: ' + str(toRec)))

            data2 = self.conn.recv(toRec)



            destinationBox = directoryIn[destModuleID]
#            log.framework_log(log.LEVEL.DEBUG, ('second message (part 2) was received, destination box is ' + str(destModuleID)))

            messageForBox = data2

            destinationBox.append(messageForBox)           


        print ('networkCom while loop ended')
        return True







        
