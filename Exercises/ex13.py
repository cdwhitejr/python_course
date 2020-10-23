#ex13.py
# YARA
'''
Create a small python code, importing the Yara module and compre the rule we already made
Create against the Lab malware provided (In kali)
Print the results of the comparison
'''
import os
import yara

rules = yara.compile(filepath='yara_rule.yar')

matches = rules.match('/root/Desktop/Malware/Lab01-02.exe')

print(matches[0].strings)