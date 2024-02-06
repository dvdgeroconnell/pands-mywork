# randomGenerator.py
# prints out a random number between start and end points provided by the user
# Author: David O'Connell, Andrew Beatty

import random

# user inputs the range (2 integers)
first = int(input("Enter the range start: "))
last = int(input ("Enter the range end: "))
number = random.randint(first,last)
print("random number is {}".format(number))