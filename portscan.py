#portscan.py
import socket


ip = 'ftp.fileviewer.com'
print(socket.gethostbyname(ip))
portlist = [69,21,22,23,80,443,445,21,3389,25,110]

for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    if result == 10060:
        print(f'{port} : {result}')
    sock.close()