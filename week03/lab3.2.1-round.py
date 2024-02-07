# round.py
# takes in a float and prints out an int rounded up or down
# Authors: David O'Connell, Andrew Beatty

x = float(input("Enter a floating point number: "))

# Comment in lab page is that round() always rounds to the nearest even number,
# however, that no longer appears to be the case.
print("{} rounded is {}".format(x, round(x)))