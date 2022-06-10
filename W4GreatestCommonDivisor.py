import math
import functools
lst=[]
while(True):
    try:
        for i in range(int(input("How many number do you want to enter"))):
            lst.append(int(input("Please enter a number")))
        print(math.gcd(*lst))
        break
    except ValueError:
        print("You haven't entered a number.Please enter a number")

