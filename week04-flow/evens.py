# evens.py
# Lab exercise for Week04-flows
# A program that uses a while loop to print all even numbers from 2 to 100
# Author: David O'Connell

num = 2
while (num <=100):

    # check if it's even (divisible by 2), and if so, print it
    if num % 2 == 0:
        print(num, sep=' ')
    num += 1