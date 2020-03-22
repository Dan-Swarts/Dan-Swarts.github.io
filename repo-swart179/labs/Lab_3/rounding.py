#This function rounds a number to the nearest integer

def roundFloat(float_number):
    if float_number >=0:
        neo_nmbr = int(float_number + 0.5)
    else:
        neo_nmbr = int(float_number - 0.5)
    return neo_nmbr

#The lines below are designed to test the roundFloat function

print(roundFloat(138.3))
print(roundFloat(8304.5))
print(roundFloat(029372.89))

print(roundFloat(-138.3))
print(roundFloat(-8304.5))
print(roundFloat(-029372.89))




        
    
