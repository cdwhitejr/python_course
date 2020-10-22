from scapy.all import *
from prettytable import PrettyTable
from collections import Counter
import plotly.graph_objects as go

def send_packet():
    #creates a packet
    packet = Ether()/IP(dst='google.com')/ICMP()

    #sends the packet
    send(packet)

def read_packet():

    #creates empty list 
    srcIP = []
    dstIP = []

    packets = rdpcap('.\HTTP_traffic.pcap')
    p_set = set()
    for pkt in packets:
        if IP in pkt:
            try:
                srcIP.append(pkt[IP].src)
                dstIP.append(pkt[IP].dst)
            except:
                pass
    
    #Create counter
    count = Counter()
    for ip in srcIP:
        count[ip] +=1

    #Create lists
    xData = []
    yData = []

    for ip, count in count.most_common():
        xData.append(ip)
        yData.append(count)
    
    #display chart
    #Resource: https://plotly.com/python/bar-charts/
    fig = go.Figure([go.Bar(x=xData,y=yData)])
    fig.show()
    
    
    def create_table():

        #create table
        table = PrettyTable(['IP','Count'])
        for ip, count in count.most_common():
            table.add_row([ip, count])
    
        print(table)



read_packet()