#reverse_lookup.py

import sys, socket

try:
    result = socket.gethostbyaddr('8.8.8.8')
    print(f'[+] The hostname is: {result[0]}')
    print(f'[+] Address:')
    for item in result[2]:
        print('-'*8,item)
except socket.herror as e:
    print('Error for resulving IP address:',e)
