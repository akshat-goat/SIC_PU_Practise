import matplotlib.pyplot as plt # FIX: Import matplotlib.pyplot

# Define sizes and labels for pie chart
sizes = [30, 20, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'green', 'purple']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Market Share of Different Brands") # Changed title to match problem statement
plt.axis('equal') # Ensures the pie chart is circular.
plt.show()
