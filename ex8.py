'''
Write a program to list all the info related to a specific file provide for the user: Size and Owner.
Python 2.7 or Python 3.8
'''
import os

#myfile = input('Please provide and absolute path to a file: ')

myfile = 'C:\Users\cdwhi\Google Drive\That Life\python_course\ex6.py'



try:
    with open(myfile) as f:
        content = f.readlines()
except FileNotFoundError as e:
    print('That file does not exist',e)
finally:
    print(os.stat(myfile))
    print(os.getcwd())