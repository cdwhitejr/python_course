from scapy.all import *
from prettytable import PrettyTable
from collections import Counter

def send_packet():
    #creates a packet
    packet = Ether()/IP(dst='google.com')/ICMP()

    #sends the packet
    send(packet)

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
    table = PrettyTable(['IP','Count'])
    for ip, count in count.most_common():
        table.add_row([ip, count])
    
    print(table)



read_packet()