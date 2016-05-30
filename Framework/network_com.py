import socket

import logging as log

class networkCom:

    def runCom(self, mailBoxesIn):

        print 'Run networkCom running'
    	# **********************************************************************************************
        # MAIN EXECUTION
        # **********************************************************************************************

        # Receives messages from the network, strips their header (length, desination), determines how much more to receive,
        # what box to send the next message to, receives the next message, and sends that to the box

        while True:
            print 'running while loop to await incoming message...'
            print ''
            print ''
  

            #receives the first segment, indicating destination module and message size
            # 1 character - control character
            # 4 characters - destination module
            # 10 characters - size of remaining message (number of characters)

            recv1, addr = self.serversocket.recvfrom(15)            

            testShutDown = int(recv1[0])
            

            lengthToRecString = recv1[5] +recv1[6] +recv1[7] + recv1[8] + recv1[9] + recv1[10] + recv1[11] + recv1[12] + recv1[13] + recv1[14] 
            lengthToRec = int(lengthToRecString)
        
            if testShutDown == 1:
                print 'shutdown message received'
                break
            destinationBox = int(recv1[1:5])
            print 'destination box is ', destinationBox

            messageForBox, addr = self.serversocket.recvfrom(lengthToRec)
            print ' second message to send is: ', messageForBox
            mailBoxesIn[destinationBox].append(messageForBox)           


        print 'networkCom while loop ended'
        return True


    def __init__(self, mailBoxes):
        log.rgb_log(log.LEVEL.VERBOSE, "Establishing Com socket")
        #establishes socket and binds it to specified port
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serversocket.bind(('', 15555))


        log.rgb_log(log.LEVEL.VERBOSE, "Com socket established")
        self.runCom(mailBoxes)

###################################################################change log to network level, not RGB level



        
