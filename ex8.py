'''
Write a program to list all the info related to a specific file provide for the user: Size and Owner.
Python 2.7 or Python 3.8
'''
import os, pwd, sys

#myfile = input('Please provide and absolute path to a file: ')

myfile = os.path.abspath('ex6.py')



try:
    with open(myfile) as f:
        content = f.readlines()
except FileNotFoundError as e:
    print('That file does not exist',e)
finally:
    filestats = os.stat(myfile)
    if filestats:
        print(f'Filename: {myfile}')
        print(f'Size in bytes: {filestats.st_size}')
        print(f'Owner: uid is {filestats.st_uid}, username is {pwd.getpwuid(filestats.st_uid).pw_name}')
    
    
