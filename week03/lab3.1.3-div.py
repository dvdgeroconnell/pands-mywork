# div.py
# read 2 numbers, divide the first by the second, provide the integer result and remainder
# Author: David O'Connell

# input() returns a string, so we need to convert to int
a = int(input("Enter first number: "))
b = int(input ("Enter second number: "))
c = a // b  # integer result
d = a % b   # remainder
print("{} divided by {} is {} with remainder {}".format(a, b, c, d))