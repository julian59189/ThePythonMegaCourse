temperatures=[10,-20,-289,100]

def cel_to_fahr(temp_in_celsius):
    if (temp_in_celsius < -273.15):
        print("That temperature doesn't make sense!")
    else:
        temp_in_fahrenheit = ((temp_in_celsius * 9) / 5) + 32
        print(temp_in_fahrenheit)
    return

for i in temperatures:
    cel_to_fahr(i)
