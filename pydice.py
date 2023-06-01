import random

user = int(input("Please input a dice number \n>>> "))

options = [4,6,8,10,12,20,30,100]

if user in options:

    output = random.randint(1,user)

    print(output)

else:

    print("INVALID!") 
