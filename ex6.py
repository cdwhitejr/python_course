#ex6.py

'''
 In Defcon you must your entrance accordingly to your years of 
 experience in Cybersecurity, in this way:

 1 - 3 years : $50
 4 - 5 years: $80
 6 - 10 years: $100
 10+ years: $200

 Create a script that show these condition and print : Your experience time
 and your admission cost.
'''


costdict = {50:list(range(1,4)), 80 : list(range(4,6)), 100 : list(range(6,11)), 200 : list(range(10,100))}


def version1():

    exp = input('Please  provide your years of experience (in years): ')

    for k,v in costdict.items():

        if int(exp) in v:
            print(f'Based on your {exp} year(s) of experience your cost is ${k}.')


def version2():
    while True:
    
    
        exp = input('Please  provide your years of experience (in years): ')

        for k,v in costdict.items():

            if exp == 'q' or exp == 'quit':
                break
        
            else:
                try:
                    if int(exp) in v:
                        print(f'Based on your {exp} year(s) of experience your cost is ${k}.')
                except ValueError:
                    print('Provide a number only')




version2()



