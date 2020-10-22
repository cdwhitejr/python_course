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

    pktdict = {}

    packets = rdpcap('.\HTTP_traffic.pcap')

    x = 0
    for pkt in packets:
        if IP in pkt:
            try:
                srcIP.append(pkt[IP].src)
                pktdict[x] = {'src_ip':pkt[IP].src, 'dst_ip':pkt[IP].dst,'src_port':pkt[TCP].sport,'dest_port':pkt[TCP].dport}
            except:
                pass
        x +=1
    
    #create table
    table = PrettyTable(['Src IP','Dest IP','Count'])
    for ip, count in count.most_common():
        table.add_row([ip, count])
    table = PrettyTable(['Src IP', 'Src Port','Dest IP', 'Dest Port'])
    for k,v in pktdict.items():
        
        table.add_row([pktdict[k]['src_ip'], pktdict[k]['dst_ip'], pktdict[k]['src_port'], pktdict[k]['dest_port']])
    

    table_text = table.get_string()

    with open('extracted_data.txt','w') as f:
        f.writelines(table_text)
           
    
    print(table)
read_packet()