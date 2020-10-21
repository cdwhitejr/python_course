#sockets

'''
Challenge:
Modify both code (server and client) to ask or wait for
IP address to connect to listen and send data
'''

# socket is an IP address and port number

import socket

# Create stream to receive data on server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Prompt User for port to listen in on
port = input('Please input the port to listen in on (9000 - 15000')

# Define server and port to listen for connections
server.bind(('localhost', port))

# Amount of connections allowed
print('Starting server')
server.listen(10)

#Give permission for the socket to receive traffic
socket_client, (host,port) = server.accept()

#Define the amount of bytes you can receive by packet
received = socket_client.recv(1024)

#print the received information
print('Received:',received)

#Provide an echo for the client
socket_client.send(received)