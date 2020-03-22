import math
import random

def estimatePi(b):
    Bruh_value = []
    for i in range(1,b):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if ((x ** 2) + (y ** 2)) <= 1:
            Bruh_value.append(1)
        else:
            Bruh_value.append(0)
    return ((sum(Bruh_value) / len(Bruh_value)) * 4)
        
        

def main():
    b = int(input("How many tests in our Monte Carlo solution?  "))
    print("My estimate is",estimatePi(b))

main()
