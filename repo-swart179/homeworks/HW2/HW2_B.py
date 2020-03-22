# CSCI 1133, Lab Section 002, HW 2, Problem B
# Daniel Swarts, swart179


def h_and_b(height,weight,age,gender):
    if gender == "f":
        BMR = 655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    if gender == "m":
        BMR = 66.5 + (13.75 * weight) + (5.00 * height) - (6.76 * age)
    return BMR
        

def r_and_s(height,weight,age,gender):
    if gender == "f":
        BMR = 447.59 + (9.25 * weight) + (3.10 * height) - (4.33 * age)
    if gender == "m":
        BMR = 88.36 + (13.40 * weight) + (4.80 * height) - (5.68 * age)
    return BMR


def m_and_s(height,weight,age,gender):
    if gender == "f":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) -161
    if gender == "m":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    return BMR


def convert_pounds_to_kg(pounds):
    kilos = pounds * 0.453592
    return kilos


def convert_inches_to_cm(inches):
    cm = inches * 2.54
    return cm

def main():
    weight = convert_pounds_to_kg(round(float(input("Weight in pounds:  ")),2))
    height = convert_inches_to_cm(round(float(input("Height in inches:  ")),2))
    age = int(input("Age:  "))
    gender = str(input("Gender: "))
    print("Your weight in kilograms:  ", round(weight,2))
    print("Your height in centimeters:  ", round(height,2))
    print("Harris and Benedict BMR:  ", round(h_and_b(height,weight,age,gender),2))
    print("Roza and Shizgal BMR:  ", round(r_and_s(height,weight,age,gender),2))
    print("Mifflin and Sons BMR:  ", round(m_and_s(height,weight,age,gender),2))

main()
