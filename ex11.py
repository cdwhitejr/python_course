#ex11.py

'''
Create a Portscanner with sockets with sockets use the gethostbyname
and the gethostbyaddr in your code
'''

import ipaddress


x = 1
iplist = []
while x <256:
    iplist.append('192.168.1.'+str(x))
    x +=1

for ip in iplist:
    #print(ip)
    pass

network_add = ''
subnet_mask = ''
host_add = ''
cidr = ''

my_add = ipaddress.ip_address('192.168.1.147')
my_net = ipaddress.ip_network('192.168.1.0/24')
print(my_net.num_addresses)

my_list = my_net.subnets()
print(my_list)