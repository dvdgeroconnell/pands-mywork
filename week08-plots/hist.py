# hist.py
# Code for histograms following along with wk08 lectures

import numpy as np
import matplotlib.pyplot as plt

# If you set a seed, the random numbers that are generated will always be the same.
np.random.seed(1)
# loc (locus), scale (range), size (number of numbers)
normdata = np.random.normal(1, 1000, 100)
print(normdata)
plt.hist(normdata)
#plt.show()


'''
xpoints = np.array(range(1,101))

ypoints = xpoints*xpoints
#ypoints = xpoints**2 also works

# This plots the ypoints against the xpoints, it doesn't plot the xpoints
plt.plot(xpoints, ypoints, label="x squared")

# Adds the label as a legend
plt.legend()

# We can also plot the xpoints
# However it will look like a flat line unless we make it a log scale
plt.plot(xpoints, xpoints, label="x", color = "green")

# The second legend() adds to the first one, it doesn't overwrite it
plt.legend()

randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label = "random")


# if you show it, the Python program keeps running until the plot window is closed
#plt.show()
plt.savefig('lecture1.png')

'''