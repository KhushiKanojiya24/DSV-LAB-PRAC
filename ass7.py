# Practical No. 7: Correlation and Regression Analysis (Salary vs Years of Experience)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import pearsonr
import statsmodels.api as sm

# Step 1: Automatically load dataset from the Downloads folder
file_path = os.path.expanduser('~/Downloads/Salary_Data.csv')
df = pd.read_csv(file_path)

# Clean column names and drop missing values
df.columns = df.columns.str.strip()
exp_col = [col for col in df.columns if 'year' in col.lower() or 'exp' in col.lower()][0]
sal_col = [col for col in df.columns if 'sal' in col.lower()][0]
df = df.dropna(subset=[exp_col, sal_col])

print(f"Using Independent Column: '{exp_col}' and Target Column: '{sal_col}'")

# Step 2: Compute Correlation Matrix
corr_matrix = df[[exp_col, sal_col]].corr()
print("\n--- Correlation Matrix ---")
print(corr_matrix)

# Step 3: Test statistical significance of correlation (Pearson r and p-value)
r_val, p_val = pearsonr(df[exp_col], df[sal_col])
print(f"\nPearson Correlation Coefficient (r): {r_val:.4f}")
print(f"P-value: {p_val:.4e}")

# Step 4: Fit Regression using statsmodels
X = sm.add_constant(df[exp_col]) 
y = df[sal_col]
ols_model = sm.OLS(y, X).fit()

# Extract key values for normal language summary
slope = ols_model.params[exp_col]
intercept = ols_model.params['const']
r2 = ols_model.rsquared
reg_pvalue = ols_model.pvalues[exp_col]

# Step 5: Visualizations (Heatmap and Regplot)
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("practical7_heatmap.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.regplot(x=exp_col, y=sal_col, data=df, color='blue', marker='o', 
            line_kws={'color': 'red', 'label': 'Regression Line'})
plt.title("Regression Plot: Salary vs Years of Experience")
plt.xlabel(exp_col)
plt.ylabel(sal_col)
plt.legend()
plt.savefig("practical7_regplot.png")
plt.close()

print("\nPlots saved successfully as 'practical7_heatmap.png' and 'practical7_regplot.png'!")