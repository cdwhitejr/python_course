#client-socket.py

'''
Challenge:
Modify both code (server and client) to ask or wait for
IP address to connect to listen and send data
'''


import socket,sys


# Create TCP/IP socket to be used to send data

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#prompt User for the IP address and port to connect to
ip = input('Please input the IP address you\'d you like to connect to: ')
port = input('Please input the port to connect to: ')

# Connect the socket  to the port where the server is going to receive data
server_add = (ip , port)

# Print what is going on
print(f'Establishing Connection to {server_add[0]} on port {server_add[1]}')

# Connect socket to server
socket.connect(server_add)

#Start connection
try:
    #Send data to server
    message = bytes(input('Please type in a message to send to the server: '))
    print(f'Sending the following data to server: {message}')
    socket.sendall(message)

    #Watch the answer
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = socket.recv(20)
        amount_received += len(data)
        print(f'Received {data}')

finally:
    print('Closing connection')
    socket.close()