print("This program calculates the base metabolic rate, or BPM ")

a_yrs = float(input("\nHow old are you? "))

def get_gender():
    gender = input("are you male or female? ")
    return gender
    

gender = get_gender()

if gender != "male" and gender != "female":
    print("please enter male or female: ")
    get_gender()

w_lbs = float(input("how much do you weigh in lbs? "))

h_inches = float(input("How tall are you in inches? "))


if gender == "female":
    BMR = 655.0 + (4.3 * w_lbs) + (4.7 * h_inches) - (4.7 * a_yrs)

if gender == "male":
    BMR = 66.0 + (6.3 * w_lbs) + (12.9 * h_inches) - (6.8 * a_yrs)

print("Your BMR is {}".format(BMR))
