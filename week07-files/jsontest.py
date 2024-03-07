# Program to write and read json to / from a file
# Author: David O'Connell, Andrew Beatty

import json

# customers is a list of dict objects
customers = [{'name' : 'Mary','amount' : 78},{'name' : 'John','amount' : 59}]

n = 0
FILENAME = "cust_list.txt"

for customer in customers:
    print(customer)
    if n == 0:
        # create the file and write the first record
        with open(FILENAME, "wt") as f:
            json.dump(customer, f)
    else:
        # append to the file
        with open(FILENAME, "at") as f:
            json.dump(customer, f)
    n+=1
    
print(f"{n} records written")
