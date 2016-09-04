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
data = conn.recv(12)
data1 = struct.unpack_from('I', data, offset=0)
data2 = struct.unpack_from('I', data, offset=4)
data3 = struct.unpack_from('I', data, offset=8)

print data1
print data2
print data3


