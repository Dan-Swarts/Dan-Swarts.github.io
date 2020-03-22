#when does f = c?

celsius = int(100)
fahrenheit = int((celsius - 32) / (5 / 9))

while fahrenheit != celsius:
    celsius = celsius - 1
    fahrenheit = int((celsius - 32) / (5 / 9))

print(celsius)
print(fahrenheit)
