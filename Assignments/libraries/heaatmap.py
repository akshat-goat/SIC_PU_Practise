import numpy as np
import matplotlib.pyplot as plt # Import matplotlib.pyplot
import seaborn as sns
import pandas as pd # Import pandas

# Problem Statement: Understanding correlations between different financial factors.
# Question: Which two variables have the highest positive correlation?

# Generate synthetic data for financial factors
# Using random normal distribution to simulate financial data with some correlation potential
np.random.seed(42) # for reproducibility
data_dict = {
    "Stock_A_Price_Change": np.random.randn(100) * 10 + 50, # Simulate price changes
    "Interest_Rate_Change": np.random.randn(100) * 0.5 + 0.1, # Simulate interest rate changes
    "Market_Sentiment": np.random.randn(100) * 2 + 5, # Simulate sentiment score
    "Volume_Traded": np.random.rand(100) * 1000 + 100, # Simulate trading volume
    "Inflation_Rate": np.random.randn(100) * 0.2 + 3 # Simulate inflation rate
}

# Add some correlation for demonstration purposes
data_dict["Stock_B_Price_Change"] = data_dict["Stock_A_Price_Change"] * 0.7 + np.random.randn(100) * 5 + 10
data_dict["Bond_Yield_Change"] = data_dict["Interest_Rate_Change"] * 0.8 - np.random.randn(100) * 0.1

# Convert dictionary to DataFrame
data_df = pd.DataFrame(data_dict)

# Compute correlation matrix
corr = data_df.corr()

# Create heatmap with correlation values
# annot=True to show correlation values on the heatmap
# fmt=".2f" to format the annotations to two decimal places
# cmap="coolwarm" for a diverging colormap
# linewidths=0.5 for lines between cells
plt.figure(figsize=(10, 8)) # Adjust figure size for better readability
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Financial Factors") # FIX: More descriptive title
plt.show()

# --- Analysis to answer the question: Which two variables have the highest positive correlation? ---
# To answer this, you would visually inspect the heatmap:
# 1. Look for the cells with the highest positive values (closest to +1.0).
# 2. Exclude the diagonal, as variables are perfectly correlated with themselves (value 1.0).
# 3. The heatmap is symmetrical, so you only need to look at one half (e.g., upper or lower triangle).

# Programmatically find the highest positive correlation (excluding self-correlation)
max_corr = -1.0
var1_max = ""
var2_max = ""

# Iterate through the correlation matrix
# Use .stack() to convert the correlation matrix to a Series, making it easier to iterate
# Filter out self-correlations (where row index == column index) and lower triangle duplicates
for (var_a, var_b), correlation_value in corr.stack().items():
    if var_a != var_b and correlation_value > max_corr:
        max_corr = correlation_value
        var1_max = var_a
        var2_max = var_b

print(f"\nAnalysis: The two variables with the highest positive correlation are '{var1_max}' and '{var2_max}' with a correlation of {max_corr:.2f}.")
