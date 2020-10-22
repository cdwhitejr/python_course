#ex12.py
'''
Use read_packet func from 'using_scapy.py' create table with src ip and dest ip
Extra: include src port and dest port
'''

from scapy.all import *
from prettytable import PrettyTable
from collections import Counter

def read_packet():

    #creates empty list 
    srcIP = []
    packets = rdpcap('.\HTTP_traffic.pcap')
    p_set = set()
    for pkt in packets:
        if IP in pkt:
            try:
                srcIP.append(pkt[IP].src)
            except:
                pass
    
    #Create counter
    count = Counter()
    for ip in srcIP:
        count[ip] +=1

    #create table
    table = PrettyTable(['Src IP','Dest IP','Count'])
    for ip, count in count.most_common():
        table.add_row([ip, count])
    
    print(table)
read_packet()