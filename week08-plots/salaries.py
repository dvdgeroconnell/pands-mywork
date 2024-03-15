# salaries.py
# Code for the wk08 labs parts 1-4 and 6

import numpy as np
import matplotlib.pyplot as plt

min = 20000
max = 80000
number = 100

# If you add this seed you get the same result each time
np.random.seed(1)

# Allow 80000 in the range
salaries = np.random.randint(min,max+1, number)
updated_salaries = salaries + 5000
increased_salaries = salaries * 1.05
# That last line created floats, so change back to ints
final_salaries = increased_salaries.astype(int)
print(salaries)
print (final_salaries)

# Plot the salaries as a histogram
plt.hist(salaries)
plt.show()
