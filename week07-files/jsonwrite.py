# Program to save a dict to a file as JSON
# Author: David O'Connell, Andrew Beatty

import json

FILENAME = "testdict.json"
# use the dict constructor
sample = dict(name = 'John', age = 31, grades = [1, 34, 45])

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)
    # return isn't always needed, only when you are returning a value.

# main program
print(sample)
write_dict(sample)
