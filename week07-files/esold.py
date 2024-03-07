# es.py
# Program to read in a text file and print out the number of e's it contains
# Author: David O'Connell

# Opening the file with "r" or "r+" throws an error if the file doesn't exist
# Assume the file exists 
# Note that r+ opens in append mode, so need to open again (the "with" closes it when done)

import os.path, sys

def read_count(sourcefile):
    return(-1)
    '''
    try:
        with open(sourcefile, "r") as f:
            x = 0
            count = 0
            content = f.read()
            while x < len(content):
                if content[x] == "e":
                    count +=1
                x+=1   
            return(count)
                
    except IOError:
        return(0)
        '''

# main program

# check if the file exists. If it doesn't, create and initialize it with 0.
# these 3 lines are not required as the try / catch in read_count will return
# a count of 0 and write_count() will create the file.

try:
    filename = sys.argv[1]

except IndexError:
    print("exception")

else:
    print(filename)

    if not os.path.isfile(filename):
        print("Not a valid file")

    else:
        final_count = read_count(filename)

        if read_count(filename) == -1:
            print("Error")
        else:
            print(final_count)