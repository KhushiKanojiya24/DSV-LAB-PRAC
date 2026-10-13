# Practical No. 3: Data Preprocessing (Missing Values & Duplicates)
import pandas as pd
import numpy as np
import os

# Step 1: Load the raw dataset from Downloads folder
file_path = os.path.expanduser('~/Downloads/students_raw.csv')
df = pd.read_csv(file_path)

print("--- Raw Dataset Preview ---")
print(df)

# Step 2: Identify missing values
print("\n--- Missing Values Count Before Cleaning ---")
print(df.isnull().sum())

# Step 3: Replace missing values in 'Attendance' using the column mean
if 'Attendance' in df.columns:
    mean_attendance = df['Attendance'].mean()
    df['Attendance'] = df['Attendance'].fillna(mean_attendance)
    print(f"\nReplaced missing Attendance values with mean: {mean_attendance:.2f}")

# Step 4: Replace missing values in 'Marks' using the column median
if 'Marks' in df.columns:
    median_marks = df['Marks'].median()
    df['Marks'] = df['Marks'].fillna(median_marks)
    print(f"Replaced missing Marks values with median: {median_marks}")

# Step 5: Check and remove duplicate records
initial_count = len(df)
duplicates_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows detected: {duplicates_count}")

df.drop_duplicates(inplace=True)
print(f"Removed {initial_count - len(df)} duplicate row(s).")

# Step 6: Verify missing values after cleaning
print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# Step 7: Export the cleaned dataset as a new CSV file
output_path = os.path.expanduser('~/Downloads/students_cleaned.csv')
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset exported successfully to: {output_path}")