import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.rand(10,10)

plt.figure(figsize=(8, 6))
sns.heatmap(data, cmap='coolwarm', annot=True, fmt=".2f", linewidths=.5)
plt.title("Heatmap of Intensity Values")
plt.xlabel("Column Index")
plt.ylabel("Row Index")
plt.show()
