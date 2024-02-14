# guess1.py
# Lab exercise for Week04-flows
# Program to ask the user to keep prompting the user to guess a number between 0 and 10 until they get it 
# Author: David O'Connell

# Error checking here could be improved - handle non-integers gracefully.

num = 5

guess = int(input("guess the number between 1 and 10: "))

while guess != num:
    guess = int(input("try again: "))

print("Well done, the number is", guess)