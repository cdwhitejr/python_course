# ex3.py

'''
Create a list of numbers from 2 to 20 (iIn any automated way), and
Print only the even numbers
'''
mylist = []
for x in range(21):

    if x % 2 == 0:
        if x == 0:
            pass
        mylist.append(x)

mylist1 = list(range(2,22,2))
print(mylist,mylist1)