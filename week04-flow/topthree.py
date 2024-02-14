# topthree.py
# Lab exercise for Week04-flows
# Program to generate 3 random numbers, (0-100), print them out, then print the top 3.
# print the numbers and their average.
# Author: David O'Connell

import random

numbers = []
topthree = []

for i in range (0,10):
    entry = random.randint(0,100)
    print(i, entry)
    numbers.append(entry)
numbers.sort(reverse=True)
print("the top 3 numbers are ", numbers[0:3], sep='', end='')