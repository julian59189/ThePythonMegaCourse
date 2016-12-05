filename = "sample.txt"

# Create empty file
def create_file():
    with open(filename,"w") as file:
        file.write("")
