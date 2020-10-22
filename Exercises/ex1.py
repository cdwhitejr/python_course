import random

'''
From a List with minimum 3 objects, print a message
including one of the list items and print that item in UPPERCASE.
print a message like: My favorite protocol is: (Protocol)
'''

plist = ['tcp','udp','ssh','ftp','tftp','snmp']

print(f'My favorite protocol is: {plist[random.randint(0,len(plist))].upper()}')