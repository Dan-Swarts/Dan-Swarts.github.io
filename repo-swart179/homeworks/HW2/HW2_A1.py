# CSCI 1133, Lab Section 002, HW 2, Problem A1
# Daniel Swarts, swart179

def subtractWhile(total,num,times):
    while times > 0:
        total = total - num
        times = times - 1
    return total

def main():
    Total = int(input("Please enter the current total:  "))
    Num = int(input("What number will be subtracted?  "))
    Times = int(input("How many times should we subtract?  "))
    print("Answer:  {0} - ({1} * {2}) = {3}".format(Total,Num,Times,subtractWhile(Total,Num,Times)))
main()
