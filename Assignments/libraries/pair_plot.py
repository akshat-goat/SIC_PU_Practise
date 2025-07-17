import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd # FIX: Import pandas

# Problem Statement: Analyzing relationships between multiple restaurant variables.
# Question: How do different variables relate to each other in the dataset, colored by 'sex'?

data_dict = {
    "total_bill": np.random.uniform(5, 50, 100),
    "tip": np.random.uniform(1, 10, 100),
    "sex": np.random.choice(["Male", "Female"], 100),
    "smoker": np.random.choice(["Yes", "No"], 100),
    "day": np.random.choice(["Thur", "Fri", "Sat", "Sun"], 100),
    "time": np.random.choice(["Lunch", "Dinner"], 100),
    "size": np.random.randint(1, 6, 100)
}

# Convert dictionary to DataFrame
data_df = pd.DataFrame(data_dict)

# Create pair plot using seaborn
sns.pairplot(data_df, hue="sex")
plt.suptitle("Pair Plot of Restaurant Data by Sex", y=1.02) # FIX: Use suptitle for overall title, adjust y
plt.show()
