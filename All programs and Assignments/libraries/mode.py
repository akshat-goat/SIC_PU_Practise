import numpy as np
from scipy import stats

# Example 1: Single Mode
my_list_1 = [1, 2, 2, 3, 3, 3, 4, 5, 5]
my_array_1 = np.array(my_list_1)

mode_result_1 = stats.mode(my_array_1)

print(f"List 1: {my_list_1}")
print(f"ModeResult for List 1: {mode_result_1}")
print(f"Mode value for List 1: {mode_result_1.mode}")
print(f"Count of mode for List 1: {mode_result_1.count}")

# Example 2: Multiple Modes (if there's a tie for the highest frequency)
# Note: Behavior for multiple modes can vary slightly between SciPy versions.
# Newer versions (1.7.0+) return an array of modes. Older versions might return only the first.
my_list_2 = [1, 2, 2, 3, 3, 4]
my_array_2 = np.array(my_list_2)

mode_result_2 = stats.mode(my_array_2)

print(f"\nList 2: {my_list_2}")
print(f"ModeResult for List 2: {mode_result_2}")
print(f"Mode value(s) for List 2: {mode_result_2.mode}") # This might be an array if multiple modes
print(f"Count of mode(s) for List 2: {mode_result_2.count}") # This might be an array if multiple modes

# Example 3: Handling potential multiple modes explicitly (more robust across SciPy versions)
my_list_3 = [1, 2, 2, 3, 3, 4, 5, 5] # 2, 3, 5 all appear twice
my_array_3 = np.array(my_list_3)

counts = np.bincount(my_array_3) # Counts occurrences of non-negative integers
# If your data is not guaranteed to be non-negative integers,
# you'd use collections.Counter as a preprocessing step or a different approach.
# For general data types, collections.Counter is more flexible than np.bincount.

max_count = np.max(counts)
all_modes_np = np.where(counts == max_count)[0]

print(f"\nList 3: {my_list_3}")
print(f"All modes for List 3 (using numpy bincount): {all_modes_np}")