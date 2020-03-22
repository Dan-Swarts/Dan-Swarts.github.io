# CSCI 1133, Lab Section 002, HW 1, Problem 1B
# Daniel Swarts, swat179

print("This program converts fahrenheit temperatures to celcius and kelvin \n")

F = float(input("Please enter the temperature in Fahrenheit: "))

C = (F - 32) * (5/9)
K = C + 273.15

print("The temperature in Celsius is: ", C)
print("The temperature in Kelvin is: ", K)

if C <= 10:
    print("It is cold!")
elif C < 23:
    print("It is nice outside!")
else:
    print("Is it just me, or is it getting hot in here?")
