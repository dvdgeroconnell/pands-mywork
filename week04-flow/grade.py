# grade.py
# Lab exercise for Week04-flows
# Author: David O'Connell

# Read a student's percentage mark and print out corresponding grade.

# use a while loop to keep accepting grades until the user enters -1
raw = 0
while raw != -1:
    raw = float(input("Enter the student's percentage grade: "))

    # In practise, percentages are rounded, i.e. 69.5 becomes 70.
    num = round(raw)
    print(num)

    if num < 0 or num > 100:
      print("invalid entry")
    elif num <= 40:
        print("Fail")
    elif num <= 49:
        print("Pass")
    elif num <= 59:
        print("Merit 2")
    elif num <=69:
        print("Merit 1")
    elif num <= 100:
        print("Distinction")
    else:
        print(f"{num} is invalid")
print("Exiting...")