# Program to try out the debugger and some list operations
# Author: David O'Connell  

ages = [12, 21, 34, 55]
sum = 0

for age in ages:
    sum += age

# print(ages[-1])
# print(ages[-3])

str = '1234567890'
print(str[::2])

print(ages)
# ages.reverse()
list.reverse(ages) #does the same thing
print(ages)

print(bin(123))