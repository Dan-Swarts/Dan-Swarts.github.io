# CSCI 1133, Lab Section 002, HW 2, Problem A2
# Daniel Swarts, swart179


def subtractFor(total,num,times):
    for i in range(0,times):
        total = total - num
    return total

def main():
    Total = int(input("Please enter the current total:  "))
    Num = int(input("What number will be subtracted?  "))
    Times = int(input("How many times should we subtract?  "))
    print("Answer:  {0} - ({1} * {2}) = {3}".format(Total,Num,Times,subtractFor(Total,Num,Times)))
main()
