#log_parser.py

import os,sys
from argparse import ArgumentParser as AP


parsed_data = []

filename = os.path.abspath('access.log')
filestats = os.stat(filename)

print(f'Filename: {filename}')
print(f'Size in bytes: {filestats.st_size}')


file = open(filename, 'r')
content = file.readlines()
print(len(content))
prev_time = ''
data = {}

for line in content:
    time = line.split('[')[1].split(']')[0].split(' ')
    status_code = line.split('"')[2].split(" ")[1]
    print(time)
    print(status_code)

file.close()


for i in parsed_data:
    print(i)