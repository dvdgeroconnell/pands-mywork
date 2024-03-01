# Program to put 10 random numbers into a queue (list),
# output all values in the queue, take the first number
# from the queue one at a time and print the number and 
# the remaining queue. 
# Author: David O'Connell  

import random

randqueue = []
new = 0
for new in range(0,10):
    randqueue.append(random.randint(1,100))

print('Queue is', randqueue)
entry = 0

for entry in range (0,len(randqueue)):
    num = randqueue.pop(0)
    print("Current number is",num,"and the queue is",randqueue)

print("The queue is now empty")
