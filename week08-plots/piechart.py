# piechart.py
# Code for pie chart following along with wk08 lectures

import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(['Apple','Orange','Banana'])
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()
