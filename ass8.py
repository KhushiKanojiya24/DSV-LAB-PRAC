# Practical No. 8: Advanced Data Preprocessing and EDA on Netflix Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Automatically load the dataset from your Downloads folder
file_path = os.path.expanduser('~/Downloads/netflix_titles.csv')
df = pd.read_csv(file_path)

# Step 2: Inspect structure with info() and isnull()
print("--- Dataset Info ---")
print(df.info())

print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

# Step 3: Handle Duplicates and Missing Values (Imputation Strategies)
initial_count = len(df)
df.drop_duplicates(inplace=True)
print(f"\nRemoved {initial_count - len(df)} duplicate row(s).")

# Imputation Strategy:
# - Fill missing text/categorical columns (director, cast, country) with 'Unknown'
# - Fill missing 'rating' with the most frequent value (mode)
for col in ['director', 'cast', 'country']:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

if 'rating' in df.columns:
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# Step 4: Data Visualization (Count Plot and Histogram)
# 1. Count Plot for Movies vs TV Shows
plt.figure(figsize=(8, 5))
if 'type' in df.columns:
    sns.countplot(x='type', data=df, palette='Set2')
    plt.title("Netflix Content Types: Movies vs TV Shows")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.savefig("practical8_count_plot.png")
    plt.close()

# 2. Histogram for Release Year Distribution
plt.figure(figsize=(10, 5))
if 'release_year' in df.columns:
    sns.histplot(df['release_year'], bins=30, kde=True, color='purple')
    plt.title("Distribution of Release Years")
    plt.xlabel("Release Year")
    plt.ylabel("Frequency")
    plt.savefig("practical8_hist_plot.png")
    plt.close()
