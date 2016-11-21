import sys

usr_inp = int(input("Enter the temperature in Degree: "))
#print("You entered: " + usr_inp)

def cel_to_fahr(temp_in_celsius):
    if (temp_in_celsius < -273.15):
        print("You entered: %d °C" % temp_in_celsius)
        print("Please enter a valid temperate")
    else:
        temp_in_fahrenheit = ((temp_in_celsius * 9) / 5) + 32
        print("Temperature in Fahrenheit: %d °F" % temp_in_fahrenheit)
    return

cel_to_fahr(usr_inp)
