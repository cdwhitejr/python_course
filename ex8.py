'''
Write a program to list all the info related to a specific file provide for the user: Size and Owner.
Python 2.7 or Python 3.8
'''
import os

file = input('Please provide and absolute path to a file: ')

try:
    with open(file) as f:
        content = f.readlines()
except FileNotFoundError as e:
    print('That file does not exist',e)

lsdir = os
