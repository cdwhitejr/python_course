#!/usr/bin/python3
import re
'''
Exercise:
Read the file /var/log/syslog
Search within the logs the ones belonging to Network and print them.
'''

import re

file = "/var/log/syslog"


with open(file, 'r') as f:
    content = f.readlines()
    

results = []
for line in content:
    if re.match(r'network',line) or re.match(r'Network',line):
        results.append(line)

for r in results:
    print(r)
