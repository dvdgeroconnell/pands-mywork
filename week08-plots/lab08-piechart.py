# lab-08 piechart.py
# Code for pie chart for lab 08 parts 11, 12

import numpy as np
import matplotlib.pyplot as plt

county_choices = ['Galway','Limerick','Dublin','Kerry','Cork']

# Pick 100 randomly from the possible counties with the frequency set in p
counties = np.random.choice(county_choices, p=[0.1, 0.3, 0.2, 0.12, 0.28], size=100)

# Now return the unique values and their respective counts as numPy arrays
unique, counts = np.unique(counties, return_counts=True)
print(unique)
print(counts)

#plt.pie(counts, labels=unique)

# Note bar is a different order to pie
plt.bar(unique, counts)
plt.show()