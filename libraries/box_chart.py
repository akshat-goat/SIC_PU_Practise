import numpy as np
import matplotlib.pyplot as plt
import random

# Problem Statement: Displaying data distribution and outliers using a box plot.
# Question: Which category has the highest spread in the dataset?

# Generate random data for 4 categories
# Each category has 100 data points
data = [np.random.randn(100) for _ in range(4)]

# Define labels for the categories on the x-axis
# We have 4 categories, so labels will be 'Category 1', 'Category 2', etc.
category_labels = [f'Category {i+1}' for i in range(len(data))]

# Create box plot
# patch_artist=True fills the boxes with color
plt.boxplot(data, patch_artist=True, labels=category_labels) # FIX: Added labels for x-axis
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Data Distribution and Outliers by Category") # FIX: More descriptive title
plt.grid(axis='y', linestyle='--', alpha=0.7) # Optional: Add a grid for better readability
plt.show()

# --- Analysis to answer the question: Which category has the highest spread? ---

# Calculate the Interquartile Range (IQR) for each category
# IQR is a common measure of statistical dispersion or spread.
# It's the difference between the 75th percentile (Q3) and the 25th percentile (Q1).
iqr_values = []
for i, category_data in enumerate(data):
    Q1 = np.percentile(category_data, 25) # Calculate 25th percentile
    Q3 = np.percentile(category_data, 75) # Calculate 75th percentile
    iqr = Q3 - Q1 # Calculate IQR
    iqr_values.append(iqr)
    print(f"Spread (IQR) for {category_labels[i]}: {iqr:.2f}")

# Find the category with the maximum IQR
max_iqr = 0
category_with_max_spread = ""

for i in range(len(iqr_values)):
    if iqr_values[i] > max_iqr:
        max_iqr = iqr_values[i]
        category_with_max_spread = category_labels[i]

# Print the result
print(f"\nConclusion: {category_with_max_spread} has the highest spread (IQR: {max_iqr:.2f}) in the dataset.")
