# guess2.py
# Lab exercise for Week04-flows
# Program to ask the user to keep prompting the user to guess a randomly generated number
# between 0 and 100 until they get it. The program tells them if they are too low or too high.
# Author: David O'Connell

# Error checking here could be improved - handle non-integers gracefully.

import random

num = random.randint(0,100)
print(num)

guess = int(input("guess the number between 0 and 100: "))

while guess != num:
    if guess > num:
        guess = int(input("too high, try again: "))
    else:
        guess = int(input("too low, try again: "))

print("Well done, the number is", guess)