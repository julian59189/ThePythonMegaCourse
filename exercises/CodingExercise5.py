temperatures=[10,-20,-289,100]

def cel_to_fahr(temp_in_celsius, f):
    if (temp_in_celsius < -273.15):
        f.write("\nPlease don't write any message in the text file when input is lower than -273.15. \n")
    else:
        temp_in_fahrenheit = ((temp_in_celsius * 9) / 5) + 32
        f.write("%d \n" % temp_in_fahrenheit)
    return

file = open("temp_F",'w')
for i in temperatures:
    cel_to_fahr(i, file)
file.close();
