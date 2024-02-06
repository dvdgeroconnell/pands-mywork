# randomfruit.py
# prints out a random fruit from a predefined list
# Authors: David O'Connell, Andrew Beatty

import random

fruits = ['Apple', 'Orange', 'Pear', 'Peach', 'Apricot', 'Lychee', 'Kiwi', 'Grape', 'Cherry']

# print the entry that corresponds to a random number in a range which is the length of the list
# remember the list range is between 0 and len-1
length = len(fruits) - 1
number = random.randint(0,length)
fruit = fruits[number]
print("fruit is {}".format(fruit))