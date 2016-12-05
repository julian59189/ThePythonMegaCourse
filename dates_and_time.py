import datetime

"""
This script creates an empty file
"""

date_time = datetime.datetime.now()
f_name = date_time.strftime("%Y-%m-%d-%H-%M-%S")

# Create empty file
def create_file():
    with open(f_name,"w") as file:
        file.write("")

create_file()
