import sys

usr_inp = int(input("Enter the temperature in Degree: "))
#print("You entered: " + usr_inp)

def cel_to_fahr(temp_in_celsius):
    temp_in_fahrenheit = ((temp_in_celsius * 9) / 5) + 32
    return temp_in_fahrenheit

usr_out = cel_to_fahr(usr_inp)
print("Temperature in Fahrenheit: %d" % usr_out)
