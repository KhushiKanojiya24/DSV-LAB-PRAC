# Practical No. 2: NumPy Array Operations & DataFrame Conversion
import numpy as np
import pandas as pd
from scipy import stats  # This line is essential for stats.mode()

# Step 1: Create a NumPy array containing numeric data
data_array = np.array([45, 55, 60, 55, 70, 85, 90, 55, 65, 80])
print("NumPy Array:", data_array)

# Step 2: Perform statistical operations (sum, mean, mode, standard deviation)
total_sum = np.sum(data_array)
mean_val = np.mean(data_array)
mode_val = stats.mode(data_array, keepdims=True).mode[0]
std_val = np.std(data_array)

print(f"\nSum: {total_sum}")
print(f"Mean: {mean_val}")
print(f"Mode: {mode_val}")
print(f"Standard Deviation: {std_val:.2f}")

# Step 3: Convert the array into a Pandas DataFrame
df = pd.DataFrame(data_array, columns=["Values"])

# Step 4: Display the first few records and summary statistics
print("\n--- First Few Records ---")
print(df.head())

print("\n--- Summary Statistics ---")
print(df.describe())