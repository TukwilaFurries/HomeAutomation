#!/usr/bin/python3
import socket
import struct
#import logging as log
import time
import select
import config
import errno
from socket import error as socket_error


# The network_com is designed to run in its own thread (it does not start this thread)
# The network_com is launched by the network_controller and handles incoming messages,
#  stripping their (length) and (destination mailbox) bits, and passing the remianing message to that mailbox
# - The initialize method creates a TCP socket and connects to the network controlller

# Parameters:
# - mailBoxesIn - a pointer to the shared mailBoxes object from the pi_controller
# - directoryIn - a pointer to the shared directory object from the pi_controller


class networkCom:

    #Creates the network com, accepting a TCP connection, and starts the main thread of execution

    def __init__(self, mailBoxesIn, directoryIn):

            self.serverTCP_IP = '10.0.0.99'
            self.TCP_PORT = config.GLOBAL.NETWORK.PIPORT
            self.directory = directoryIn
            

            self.connectCom()           
            self.runCom(mailBoxesIn, directoryIn)

    # Receives messages from the network, strips their header (length, desination), determines how much more to receive,
    # what box to send the next message to, receives the next message, and sends that to the box

    def runCom(self, mailBoxesIn, directoryIn):


        #receives the first 8 byte segment:
        # -[0]indicating how many bytes of remaining message to be received (32 bits unsigned int) 
        # -[1]indicating destination module (32 bits unsigned int)


        while True:
            print("Network Com awaiting incoming message...")
            time.sleep(.2)

            #for reference, message to be passed to light module
            # 1 character - control character
            # 4 characters - destination module
            # 10 characters - size of remaining message (number of characters)

            data = self.inboundSocket.recv(8)
            while (not data):
                print ('***************CONNECTION LOST***************')
                self.inboundSocket.close()
                print ('attempting reconnect...')
                self.connectCom()
                data = self.inboundSocket.recv(8)

                
            data = struct.unpack('II', data)
            destModuleID = data[1]
            toRec = data[0]
            print('network com received new message (part 1), number of bytes to receive for payload is: ' + str(toRec))

            data2 = self.inboundSocket.recv(toRec)

            destinationBox = directoryIn[destModuleID]
            print('second message (part 2) was received, destination box is ' + str(destModuleID))

            messageForBox = data2

            destinationBox.append(messageForBox)           


        print ('networkCom while loop ended')
        return True



    def connectCom(self,):


        self.inboundSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connected = False

        while(not connected):

            try:
                self.inboundSocket.connect((self.serverTCP_IP, self.TCP_PORT))
                connected = True
            except socket_error as serr:
                if serr.errno != errno.ECONNREFUSED:
                    # If a different error than "connection refused", raise error
                    raise serr
                else:
                    print("[network com]: unable to connect to network_controller, waiting and trying again")
                    time.sleep(3)
            
            if(connected):
                print("[network com] connection to network controller sucessful")




        
