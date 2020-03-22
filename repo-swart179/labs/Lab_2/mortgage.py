#This progam helps calculate loan payments

a = float(input("enter your loan amount (how much do you owe?)"))
r = float(input("enter your annual interest rate"))
n = float(input("enter your loan time in months"))

payment = (r * a) / (1 - (1 + r) ** (n * -1))

print("you owe", payment, "every month")
