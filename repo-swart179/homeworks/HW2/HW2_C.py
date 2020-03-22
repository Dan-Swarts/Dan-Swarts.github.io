# CSCI 1133, Lab Section 002, HW 2, Problem B
# Daniel Swarts, swart179

def forecast():
    Q1 = input("Is the temperature above 70 fahrenheit?  ")
    if Q1 == "yes":
        Q2 = input("Is the wind blowing faster than 2 mph?  ")
        if Q2 == "yes":
            Q3 = input("Is the air pressure above 26 inHg?  ")
            if Q3 == "yes":
                answer = "Rain"
            if Q3 == "no":
                answer = "No rain"
        if Q2 == "no":
            answer = "No rain"
    if Q1 == "no":
        Q2 = input("Is the wind blowing faster than 4.5 mph?  ")
        if Q2 == "yes":
            answer = "Rain"
        if Q2 == "no":
            Q3 = input("Is the air pressure above 31inHg?  ")
            if Q3 == "yes":
                answer = "Rain"
            if Q3 == "no":
                answer = "No rain"
    return answer

def main():
    print(forecast())
main()
