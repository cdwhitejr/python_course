'''
Challenge:
Create a program to detect the operating system you use and then execute the
ping command accordingly like this:
Windows: ping -n 1 127.0.0.1
Linux: ping -c 1 127.0.0.1
Mac: ping -c 1 127.0.0.1
'''

import os, sys, platform, subprocess



os_systemsdict = {'Windows': ['ping', '-n', '1', '127.0.0.1'], 'Linux': ['ping','-c','1', '127.0.0.1'], 'Mac': ['ping','-c','1', '127.0.0.1']}

print(f'You are running: {platform.system()}, will now ping using the {platform.system()} command')

if os_systemsdict[platform.system()]:
    subprocess.run(os_systemsdict[platform.system()])
