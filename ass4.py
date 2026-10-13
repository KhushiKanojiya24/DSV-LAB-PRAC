# Ass 4: Load Netflix Dataset, Clean Data and Save Graph Image
import pandas as pd
import matplotlib.pyplot as plt
import os

# Netflix file path from Downloads folder
file_path = os.path.expanduser('~/Downloads/netflix_titles.csv')

# Load dataset
df = pd.read_csv(file_path)

# Display first few records
print("First few records of the dataset:")
print(df.head())

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna("Unknown", inplace=True)

# Plot a bar graph (Movies vs TV Shows count)
df["type"].value_counts().plot(kind="bar", color=["skyblue", "salmon"])
plt.title("Netflix Movies vs TV Shows Count")
plt.xlabel("Type")
plt.ylabel("Count")

# Save the plot as an image file in your folder
plt.savefig("netflix_plot.png")
plt.close()

print("Graph saved successfully as 'netflix_plot.png' in your folder!")