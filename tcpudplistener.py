import socket
import os
import sys


UDP_IP = "0.0.0.0"
UDP_PORT = int(os.environ['UDPPORT'])

print "Listening on UDP port",UDP_PORT

udpsock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
udpsock.bind((UDP_IP, UDP_PORT))



TCP_IP = "0.0.0.0"
TCP_PORT = int(os.environ['TCPPORT'])

print "Listening on TCP port",TCP_PORT

tcpsock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # TCP
tcpsock.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
tcpsock.listen(1)


while True:
    udpdata, addr = udpsock.recvfrom(1024) # buffer size is 1024 bytes
    print udpdata

    # Wait for a TCP connection
     print >>sys.stderr, 'waiting for a connection'
    connection, client_address = tcpsock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            tcpdata = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % tcpdata
            if tcpdata:
                connection.sendall(tcpdata)
            else:
                break
    finally:
        connection.close()