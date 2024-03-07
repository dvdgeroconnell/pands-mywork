# Program to save a dict to a file as JSON
# Author: David O'Connell, Andrew Beatty

import json

FILENAME = "testdict.json"
# use the dict constructor

def read_dict():
    with open(FILENAME, 'rt') as f:
        return json.load(f)

# main program
sample = read_dict()
print(sample)