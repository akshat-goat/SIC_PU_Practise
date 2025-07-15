import numpy as np
import matplotlib.pyplot as plt
import random

# Problem Statement: Comparing multiple distributions using a violin plot.
# Question: How does the density of data differ across categories?

# Generate random data for 4 categories (as used in the previous box plot example)
# Each category has 100 data points
data = [np.random.randn(100) for _ in range(4)]

# Define labels for the categories on the x-axis
# We have 4 categories, so labels will be 'Category 1', 'Category 2', etc.
category_labels = [f'Category {i+1}' for i in range(len(data))]

# Create violin plot
# 'data' is the list of arrays for each category
# 'showmeans=True' adds a marker for the mean of each distribution
# 'showmedians=True' adds a marker for the median of each distribution
plt.violinplot(data, showmeans=True, showmedians=True) # FIX: Removed 'labels' from here
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Density Distribution Across Categories (Violin Plot)") # FIX: More descriptive title
plt.grid(axis='y', linestyle='--', alpha=0.7) # Optional: Add a grid for better readability

# FIX: Set x-axis tick labels using plt.xticks() after the plot is created
# The tick locations are 1, 2, 3, 4 for the 4 categories
plt.xticks(np.arange(1, len(data) + 1), category_labels)

plt.show()