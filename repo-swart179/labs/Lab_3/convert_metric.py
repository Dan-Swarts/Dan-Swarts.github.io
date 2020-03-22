print("This file converts metric units\n")


def convert_metric():
    value = float(input("Enter value: "))
    units = str(input("Enter units: "))

    if units == "pounds":
        nw_value = value * 1.3607772
        nw_unit = "kilos"
        print(nw_value,nw_unit)

    elif units == "kilos":
        nw_value = value / 1.3607772
        nw_unit = "pounds"
        print(nw_value,nw_unit)

    elif units == "ounces":
        nw_value = value * 85.04856
        nw_unit = "grams"
        print(nw_value,nw_unit)

    elif units == "grams":
        nw_value = value / 85.04856
        nw_unit = "ounces"
        print(nw_value,nw_unit)

    elif units == "miles":
        nw_value = value * 1.609344
        nw_unit = "kilometers"
        print(nw_value,nw_unit)

    elif units == "kilometers":
        nw_value = value / 1.609344
        nw_unit = "miles"
        print(nw_value,nw_unit)

    elif units == "inches":
        nw_value = value * 2.54
        nw_unit = "centimeters"
        print(nw_value,nw_unit)

    elif units == "centimeters":
        nw_value = value / 2.54
        nw_unit = "inches"
        print(nw_value,nw_unit)

    else:
        print("{} is not a valid unit".format(units))

convert_metric()



done = str(input("do you wish to continue (y/n)? "))
if done == y:
    convert_metric()
elif continue_chekc != y and continue_check != n:
    print("bruh")
