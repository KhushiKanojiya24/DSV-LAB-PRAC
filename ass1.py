# Practical No. 1: Create a dataset of student marks, calculate average, maximum, and minimum marks, and display it using Python libraries.
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the dataset of student marks
data = {
    "Roll_No": [1, 2, 3, 4, 5, 6, 7, 8],
    "Student_Name": ["Amit", "Sneha", "Rahul", "Priya", "Om", "Sakshi", "Yash", "Rutuja"],
    "Marks": [78, 92, 55, 88, 64, 95, 47, 81]
}
df = pd.DataFrame(data)

# Step 2: Display dataset
print("--- Student Marks Dataset ---")
print(df)

# Step 3: Compute descriptive statistics
avg_marks = df['Marks'].mean()
max_marks = df['Marks'].max()
min_marks = df['Marks'].min()

print(f"\nAverage Marks: {avg_marks}")
print(f"Maximum Marks: {max_marks}")
print(f"Minimum Marks: {min_marks}")

# Step 4: Visualize the results
plt.figure(figsize=(8, 5))
plt.bar(df['Student_Name'], df['Marks'], color='skyblue')
plt.title("Student Marks Bar Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.savefig("practical1_plot.png")
plt.close()
print("\nPlot saved successfully as 'practical1_plot.png'")