#ex2.py
'''
From a list select on of the items and assign that objec to a variable
and remove it from that list, and print a message including that 
removed item.
'''

plist = ['tcp','udp','ssh','ftp','tftp','snmp']


print(f'\nPlease choose one of the items from the following list to be removed: {plist}')

rem = input('Which item would you liked removed?')

if rem in plist:
    plist.remove(rem)
    print(f"You've removed {rem} from the list.\nHere's your new list: {plist}")
else:
    print(f"You entered in {rem}, that was not a valid option.")