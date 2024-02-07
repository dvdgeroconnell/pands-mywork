# convert.py
# takes in a currency number (positive or negative) and returns the absolute amount in cent
# Authors: David O'Connell

# requires floor() which is a method in the math module, not a built-in function
import math

# read the amount as a float, as instructed
# for an assignment, I would do more error checking around having a decimal point with 2 decimal places.
raw_amount = float(input("Enter an amount in dollars and cents: "))
raw_amount = abs(raw_amount)
dollar = math.trunc(raw_amount)
print (f"dollar amount is: {dollar}")
dollar_to_cent = dollar * 100
length = len(str(raw_amount))
# note the last character is not included
cents = str(raw_amount)[length-2:length]
print(f"cent amount is: {cents}")

print(f"The absolute amount in cent is: {dollar_to_cent + int(cents)}")