# sub.py
# read 2 numbers, subtract the first from the second and print the result
# Author: David O'Connell

# input() returns a string, so we need to convert to int
a = int(input("Enter first number: "))
b = int(input ("Enter second number: "))
c = b - a
print("{} minus {} is {}".format(b, a, c)) 

