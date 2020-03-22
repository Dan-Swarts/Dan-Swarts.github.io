#This program will simulate the tossing of two dice 10,000 times

#import the ability to generate random numbers:

import random
from random import randint

dice_list = []
test_list = []

for x in range(0,10000):
    n = randint(1,6) + randint(1,6)
    dice_list.append(n)
    

for num in range (2,13):
    for n in range(0,10000):
        if dice_list[n] == num:
            test_list.append(0)
    print("{0:2d}:{1:5d}".format(num, len(test_list)))
    test_list.clear()
