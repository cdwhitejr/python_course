#ex5.py
'''
Challenge 1:
Create a list with 4 items; then print each object with a cycle and
add the message you prefer for each print; separate with new line feed each print

Challenge 2:
Create a list with 6 items and then print with a cycle the first 3 items.

'''


#Challenge 1
list1 = ['tcp','udp','ssh','telnet']
for proto in range(len(list1)):
    print(f'The protocol is {list1[proto]}.')

#Challenge 2
list2 = sorted([22,23,21,80,25,443])
print(f"list2 is {list2}")
print("Only printing the first 3 items")
for x in range(0,3):
    print(f"Item {x} is {list2[x]}.")


