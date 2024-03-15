# labplots.py
# Code for wk08 lab part 5 - plot the function y = x^2

import numpy as np
import matplotlib.pyplot as plt

min = 1
max = 50

x = np.array(range(min, max))
y = x**2
# This plots the ypoints against the xpoints, it doesn't plot the xpoints
plt.plot(x, y, label="x squared")
plt.plot(x, x, label="x", color = "green")

# Adds the labels as a legend
plt.legend()

# We can also plot the xpoints
# However it will look like a flat line unless we make it a log scale

plt.show()
#plt.savefig('lecture1.png')

