#!/usr/bin/python3
'''
Exercise:
Read the file /var/log/syslog
Search within the logs the ones belonging to Network and print them.
'''

import re, sys

try:
    file = sys.argv[1]
except:
    print('provide a valid file')
finally:
    file = "/var/log/syslog"


print('Reading...')
with open(file, 'r') as f:
    content = f.readlines()
    
print('Pulled content...')
results = []


for line in content:
    if 'network' in line.lower():
        results.append(line)

for r in results:
    pass
    print(r)
