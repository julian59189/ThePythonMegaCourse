import datetime

"""
This script merges three files
"""

date_time = datetime.datetime.now()
f_name = date_time.strftime("%Y-%m-%d-%H-%M-%S-%f")
file =  open(f_name + ".txt","w")

files = ["Sample-Files/file1.txt", "Sample-Files/file2.txt", "Sample-Files/file3.txt"]
for i in range (0, 3):
    with open(files[i],"r") as f_in:
        text = f_in.read()
        file.write(text + "\n")
