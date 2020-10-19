#ex4.py
'''
With a cycle print the power of 2 for the first 10 numbers 1 to 10
'''
x = 1
while x <=10:
    print(x**2)
    x +=1


power2 = [value ** 2 for value in range(1,11)]
print(f"Power of 2: {power2}")



# my extra playing around
mydict = {}
x = 1
while x <= 10:
    templist = []
    templist = [value ** x for value in range(1,11)]
    mydict[x] = templist
    x += 1

for n,l in mydict.items():
    print(f"Power of {n} : {l}")