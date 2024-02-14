# average.py
# Lab exercise for Week04-flows
# Program to keep reading numbers until the user enters a 0. Append them to a list,
# print the numbers and their average.
# Author: David O'Connell

# Error checking here could be improved - handle non-integers gracefully.

entry = int(input("input an integer, 0 to finish: "))
i = 0
numbers = []

while entry != 0:
    numbers.append(entry)
    i += 1
    entry = int(input("input another integer, 0 to finish: "))

total = 0

for number in numbers:
    print(number, sep=" ", end = ' ')
    total = total + number
print("\nthe average is", total/i)
avg = float(sum(numbers)/len(numbers))
print("the average using list functions is", avg)