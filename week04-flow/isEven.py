# isEven.py
# Lab exercise for Week04-flows
# Author: David O'Connell

# Error checking here could be improved - handle non-integers gracefully.

num = int(input("Enter a non-zero integer: "))
if (num == 0):
    print("Invalid entry.")
elif (num % 2) == 0:    
    str = 'even'
else:
    str = 'odd'

# only print this line if num is not 0.

if num:
    print(f"That number is {str}.")