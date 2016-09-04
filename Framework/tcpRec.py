#!/usr/bin/python
import socket
import time
import struct

TCP_IP = '10.0.0.98'
TCP_PORT = 15555
BUFFER_SIZE = 1024

print 'running, waiting for message'


#establishes socket and binds it to specified port
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((TCP_IP,TCP_PORT))
serversocket.listen(1)
conn, addr = serversocket.accept()
print 'Connection address:', addr
data = conn.recv(8)
data = struct.unpack('II', data)
destModuleID = data[0]
toRec = data[1]
print toRec

data2 = conn.recv(toRec)
print struct.unpack_from('I', data2, offset=0), struct.unpack_from('I', data2, offset=4), struct.unpack_from('I', data2, offset=8), struct.unpack_from('I', data2, offset=12), struct.unpack_from('I', data2, offset=16)



print 'done'
