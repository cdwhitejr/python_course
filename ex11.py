#ex11.py

'''
Create a Portscanner with sockets with sockets use the gethostbyname
and the gethostbyaddr in your code

ip = 'ftp.fileviewer.com'
print(socket.gethostbyname(ip))
portlist = [69,21,22,23,80,443,445,21,3389,25,110]

for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    if result == 10060:
        print(f'{port} : {result}')
    sock.close()
'''

import socket,ipaddress,sys,os
from threading import Thread


def scanport(port):
    pass



# get ip address or network range
if len(sys.argv) >= 2:
    print(sys.argv)
# get desired port or port range


# create function that tests desired port

#determine 1 or more ports

# create thread to handle multiple ip addresses at once

#determine 1 or more ip addresses given