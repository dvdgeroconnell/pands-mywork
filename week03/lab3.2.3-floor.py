# floor.py
# takes in a float number and rounds it down
# Authors: David O'Connell, Andrew Beatty

# requires floor() which is a method in the math module, not a built-in function
import math

# read in the float
x = float(input("Enter a floating point number: "))

# Use math method floor()
print("Rounded-down value of {} is {}".format(x, math.floor(x)))