#ipaddress_play.py

import ipaddress


my_add = ipaddress.ip_address('192.168.1.147')
my_net = ipaddress.ip_network('192.168.1.0/24')
print(my_net.num_addresses)


# returns all valid host ip addr in net
for addr in my_net.hosts():
    print(addr)

# checks if ip add in net
if my_add in my_net:
    print(True)

#splits possible subnets with prefixlen_diff
my_list = list(my_net.subnets(prefixlen_diff=4))
print(f'Created {len(my_list)} subnets. They are as follows:\n')
for sub in my_list:
    print(f'{sub} with {sub.num_addresses} hosts in each subnet.')

