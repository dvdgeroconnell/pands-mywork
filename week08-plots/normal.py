# agesalaries.py
# Code for the wk08 labs parts 7, 8

import numpy as np
import matplotlib.pyplot as plt

min = 20000
max = 80000
number = 100
min_age = 21
max_age = 65

# Add this seed to get the same result each time
np.random.seed(1)

# Now create an array of numbers 'x' and the squares 'y' and add to the plot
xpoints = np.array(range(1,101))

plt.xlabel('ages, x')
plt.ylabel('salaries, x-squared')
plt.title('Lab 08')

# Add a normal distribution line to lab 9
loc = ((max_age+1 - min_age)/2 + min_age)
scale = (max_age+1 - min_age)/3
print("locus=",loc)
print("scale=",scale)

norm = np.random.normal(loc, scale, 1000)

print(norm)
plt.hist(norm, label="normal", color='g')
plt.plot(norm, label="normal", color='g')


plt.legend()
plt.show()
# Part 10
# plt.savefig('prettier-plot.png')