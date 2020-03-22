#this program finds windchill,
#given temerature and wind speed

t = float(input("enter a temperature in degrees Fahrenheit"))
v = float(input("how fast is the wind going in mph?"))

windchill = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
 
print('including wind chil, the temperature is' + str(windchill) + 'degrees Fahrenheit')
