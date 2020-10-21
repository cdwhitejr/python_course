#portscan.py
'''
Basic:

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
from argparse import ArgumentParser



# creates argeparse environment
def parser_creation():
        
    parser = ArgumentParser(prog='ex11.py')
    
    
    parser.add_argument('-p',dest='port', help='Insert desired port [21]', type=int, nargs=1)
    parser.add_argument('-pr',dest='port_range', nargs=2,help='Insert desired port range [21 50]',required=False,type=int, action='append')
    parser.add_argument('-net', dest='network',type=ipaddress.ip_network, help='Insert valid IPv4/6 network address with CIDR')
    parser.add_argument('-ip',dest='host',type=ipaddress.ip_address,help='Insert valid IPv4/6 host address')

    if len(sys.argv) == 1:
        parser.print_help()
    else:
        parser.parse_args()

parser_creation()
# get ip address or network range


# get desired port or port range


# create function that tests desired port
def scanport(port):
    pass

#determine 1 or more ports

# create thread to handle multiple ip addresses at once

#determine 1 or more ip addresses given