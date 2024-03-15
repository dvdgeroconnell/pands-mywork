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

# Allow max salary in the range
salaries = np.random.randint(min,max+1, number)

# Allow max age in the list
ages = np.random.randint(min_age,max_age+1, number)

updated_salaries = salaries + 5000
increased_salaries = salaries * 1.05
# That last line created floats, so change back to ints
final_salaries = increased_salaries.astype(int)

print(ages)
print(salaries)

# Plot the ages and salaries as a scatter plot
plt.scatter(ages, salaries, label='salaries v ages')

# Now create an array of numbers 'x' and the squares 'y' and add to the plot
xpoints = np.array(range(1,101))
ypoints = xpoints*xpoints

# This plots the ypoints against the xpoints, it doesn't plot the xpoints
plt.plot(xpoints, ypoints, label="x squared", color = 'r')

plt.xlabel('ages, x')
plt.ylabel('salaries, x-squared')
plt.title('Lab 08')

plt.legend()
plt.show()
# Part 10
# plt.savefig('prettier-plot.png')