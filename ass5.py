# Practical No. 5: Data Preprocessing and Exploratory Data Analysis on Netflix Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Automatically load the dataset directly from your Downloads folder
file_path = os.path.expanduser('~/Downloads/netflix_titles.csv')
df = pd.read_csv(file_path)

# Step 2: Inspect structure with info(), describe(), and isnull()
print("--- Dataset Info ---")
print(df.info())

print("\n--- Descriptive Statistics ---")
print(df.describe(include='all'))

print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Step 3: Data Cleaning (Handle duplicates and missing values)
initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"\nRemoved {initial_rows - len(df)} duplicate row(s).")

# Imputation strategy for categorical column 'rating'
if 'rating' in df.columns:
    df['rating'] = df['rating'].fillna("TV-MA")

# Step 4: Data Visualization (Count Plot and Histogram)
# Count Plot for Movies vs TV Shows
plt.figure(figsize=(8, 5))
if 'type' in df.columns:
    sns.countplot(x='type', data=df, palette='Set2')
    plt.title("Netflix Movies vs TV Shows Count Plot")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.savefig("practical5_count_plot.png")
    plt.close()

# Histogram for Release Year distribution
plt.figure(figsize=(8, 5))
if 'release_year' in df.columns:
    sns.histplot(df['release_year'], bins=30, kde=True, color='teal')
    plt.title("Histogram of Release Years")
    plt.xlabel("Release Year")
    plt.ylabel("Frequency")
    plt.savefig("practical5_hist_plot.png")
    plt.close()

print("\nEDA completed successfully! Plots saved as 'practical5_count_plot.png' and 'practical5_hist_plot.png'.")