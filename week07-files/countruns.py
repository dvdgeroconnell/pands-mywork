# countruns.py
#counts how many times it was run
# Author: David O'Connell

# Opening the file with "r" or "r+" throws an error if the file doesn't exist
# Assume the file exists 
# Note that r+ opens in append mode, so need to open again (the "with" closes it when done)

import os.path

FILENAME = "count.txt"

def read_count():
    try:
        with open(FILENAME, "r") as f:
            count = int(f.read())
        return(count)
    except IOError:
        return(0)

def write_count(count):
    with open(FILENAME, "w") as f:
        f.write(str(count)) # returns the number of chars written
    return

# main program

# check if the file exists. If it doesn't, create and initialize it with 0.
# these 3 lines are not required as the try / catch in read_count will return
# a count of 0 and write_count() will create the file.
if not os.path.isfile(FILENAME):
    print("Creating file")
    write_count(0)

number = read_count()
number +=1
print(f"The program has been run {number} times.")
write_count(number)
