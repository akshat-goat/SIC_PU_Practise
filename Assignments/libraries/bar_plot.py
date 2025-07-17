
# Problem Statement: Comparing categorical data using a bar chart.
# Question: Which category has the highest value in the given dataset?

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

cars = ['Ferrari', 'Lamborghini', 'Aston Martin', 'Dolorean']
values = [10, 20, 15, 25]

plt.bar(cars, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Cars")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.show()