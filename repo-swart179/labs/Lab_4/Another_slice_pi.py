import math

def tolerance_check(a,b,c):
    if (a - b) < c:
        return "stop"
    else:
        return "go"

def estimatePi(tolerance):
    pi_list = [1,-1 / 9]
    n = 1
    m = 3
    previous = sum(pi_list)
    value = previous
    x = "go"
    while x == "go":
        previous = value
        n = n + 1
        m = m + 2
        append.pi_list(1 /  (3 ** n * m))
        value = (6 / sqrt(3)) * sum(pi_list)
        x = tolerance_check(value,previous,tolerance)
    return value

def main():
    tol = float(input("enter your tolerence:  "))
    print(estimatePi(tol))
main()
