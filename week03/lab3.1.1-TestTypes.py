# Lab 3.1 variables and state
# Author David O'Connell

#define the different variables
i = 3
fl = 3.5
isa = True
memo = "Dave"

# 2 options to create the list. Use the constructor
#lots = ["John", "Stephen", "Mary", "Catherine"]
lots = list(("John", "Stephen", "Mary Smith", "Catherine"))

# my method before I read the full lab instructions!
'''
#print the variable types and values
print(f"variable i is of type: {type(i)} and value = {i}")
print(f"variable fl is of type: {type(fl)} and value = {fl}")
print(f"variable isa is of type: {type(isa)} and value = {isa}")
print(f"variable memo is of type: {type(memo)} and value = {memo}")
print(f"variable lots is of type: {type(lots)} and value = {lots}")
'''
# Andrew's method in the lab instructions
print('variable {} is of type: {} and value: {}'.format('i', type(i), i))
print('variable {} is of type: {} and value: {}'.format('fl', type(fl), fl))
print('variable {} is of type: {} and value: {}'.format('isa', type(isa), isa))
print('variable {} is of type: {} and value: {}'.format('memo', type(memo), memo))
print('variable {} is of type: {} and value: {}'.format('lots', type(lots), lots))