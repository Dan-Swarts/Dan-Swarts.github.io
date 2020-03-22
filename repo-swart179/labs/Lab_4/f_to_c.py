#This program converts fahrenheit to celsius, and vice versa

value = int(input("enter temp:  "))
cont = str(input("enter f or c:  "))

if cont == "f":
    celsius = int((value - 32) / (5 / 9))
    fahrenheit = value
    print("Your value in celsius is :",celsius)

if cont == "c":
    fahrenheit = int((9 / 5) * celsius + 32)
    celsius = value
    print("Your value in fahrenheit is: ",fahrenheit)

