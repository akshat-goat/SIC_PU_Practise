import pandas as pd

# This DataFrame created from a dictionary is immediately overwritten by pd.read_csv.
# If you intend to use this data, remove the pd.read_csv line below.
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df_from_dict = pd.DataFrame(data)
print("DataFrame created from dictionary (will be overwritten):")
print(df_from_dict)
print("-" * 30) # Separator for clarity

import os
file_path = r'D:\LEARNING\SIC_PU_Practise\data\data.csv'

if os.path.exists(file_path):
    print(f"File exists at: {file_path}")
else:
    print(f"File DOES NOT exist at: {file_path}")
    print("Please check the path and filename carefully.")
    # You can also list directory contents to see what's there
    # print("Contents of data directory:")
    # print(os.listdir(r'D:\LEARNING\SIC_PU_Practise\data'))

# FIX: Using a raw string literal (r'...') for the file path
# This prevents backslashes from being interpreted as escape characters.
# Ensure 'data.csv' actually exists at this exact path.
df = pd.read_csv(r'D:\LEARNING\SIC_PU_Practise\data\data.csv')

print("\nDataFrame loaded from 'data.csv' (this is the active DataFrame 'df'):")
print(df.head()) # Displays the first 5 rows (or fewer if less than 5)

print("\nMissing values in DataFrame from CSV:")
print(df.isnull().sum()) # Counts missing values in each column

print("\nRows where 'Salary' is greater than 50000 (from CSV DataFrame):")
high_salary = df[df['Salary'] > 50000] # Filters rows based on Salary
print(high_salary)

print("\nDataFrame from CSV sorted by 'Salary' in descending order:")
df_sorted = df.sort_values(by='Salary', ascending=False)
print(df_sorted)
