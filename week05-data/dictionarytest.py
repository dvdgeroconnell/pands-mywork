# Program to try out dictionaries
# Author: David O'Connell  

# use the dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December")

summer = months[4:7]
print(type(summer))

for month in summer:
    print(month)


'''
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
'''