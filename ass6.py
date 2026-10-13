# Practical No. 6: Simple Linear Regression (Salary vs Years of Experience)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Step 1: Automatically load dataset from the Downloads folder
file_path = os.path.expanduser('~/Downloads/Salary_Data.csv')
df = pd.read_csv(file_path)

# Strip any accidental spaces from column names
df.columns = df.columns.str.strip()

# Automatically identify columns dynamically
exp_col = [col for col in df.columns if 'year' in col.lower() or 'exp' in col.lower()][0]
sal_col = [col for col in df.columns if 'sal' in col.lower()][0]

# Drop rows with missing values (NaN) to prevent regression errors
df = df.dropna(subset=[exp_col, sal_col])

print(f"Using Independent Column: '{exp_col}' and Target Column: '{sal_col}'")

X = df[[exp_col]]
y = df[sal_col]

# Step 3: Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Fit Simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Interpret slope and intercept
print(f"\nSlope (b₁): {model.coef_[0]:.2f}")
print(f"Intercept (b₀): {model.intercept_:.2f}")

# Step 5: Evaluate model with R², MAE, and RMSE
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n--- Model Evaluation ---")
print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# Step 6: Predict value for a new input (e.g., 5.5 years of experience)
new_experience = np.array([[5.5]])
predicted_salary = model.predict(new_experience)
print(f"\nPredicted Salary for 5.5 years of experience: ${predicted_salary[0]:,.2f}")

# Step 7: Plot data and regression line, then save as PNG for macOS stability
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title("Simple Linear Regression: Salary vs Years of Experience")
plt.xlabel(exp_col)
plt.ylabel(sal_col)
plt.legend()

plt.savefig("practical6_plot.png")
plt.close()
print("\nRegression plot saved successfully as 'practical6_plot.png'!")