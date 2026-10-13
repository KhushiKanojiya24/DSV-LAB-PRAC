# Script to generate sample raw dataset 'students_raw.csv'
import pandas as pd
import numpy as np

data = {
    "Roll_No": [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10],
    "Student_Name": ["Amit", "Sneha", "Rahul", "Priya", "Om", "Sakshi", "Yash", "Rutuja", "Rutuja", "Kunal", "Isha"],
    "Attendance": [85, 90, np.nan, 78, 88, 92, np.nan, 75, 75, 95, 82],
    "Marks": [78, 85, 90, np.nan, 88, 76, 92, 65, 65, np.nan, 80]
}

df = pd.DataFrame(data)

# Save as students_raw.csv directly in Downloads or workspace folder
import os
file_path = os.path.expanduser('~/Downloads/students_raw.csv')
df.to_csv(file_path, index=False)
print(f"Raw dataset created and saved successfully at: {file_path}")