# extra.py
# extra content from lab
# Author: David O'Connell

# why does the given expression cause an error
# message = 'I have eaten ' + 99 + ' burritos.'
# because you cannot concatenate int to str
# this works
message = 'I have eaten ' + str(99) + ' burritos.'
print(message)
# and this works
print('I have eaten {} burritos.'.format(99))

# eggs isa valid variable name while 100 is not, because
# 100 starts with an integer which is not supported

# the functions to get the integer, floating point and string
# version of a value are:
i = 99
print ("integer = {}".format(int(i)))
print ("float = {}".format(float(i)))
print ("string = {}".format(str(i)))