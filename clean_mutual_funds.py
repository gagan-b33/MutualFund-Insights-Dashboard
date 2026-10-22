import pandas as pd
import numpy as np

# 1. Load the raw dataset
df = pd.read_csv('comprehensive_mutual_funds_data.csv')

# 2. Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# 3. Convert numeric columns (handling potential string formats or blanks)
numeric_cols = ['min_sip', 'min_lumpsum', 'expense_ratio', 'fund_size_cr', 'fund_age_yr', 
                'alpha', 'sd', 'beta', 'sharpe', 'returns_1yr', 'returns_3yr', 'returns_5yr']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 4. Handle Missing Values (Real-world data wrangling)
# Fill missing 5-year returns with 3-year returns (logical proxy for newer funds)
df['returns_5yr'] = df['returns_5yr'].fillna(df['returns_3yr'])

# Fill missing Sharpe ratios with 0 (neutral risk-adjusted performance)
df['sharpe'] = df['sharpe'].fillna(0)

# Drop rows where critical data (like fund name or category) is missing
df = df.dropna(subset=['scheme_name', 'category', 'amc_name'])

# 5. Feature Engineering: Create a "Risk-Adjusted Score"
# Formula: (3-Year Return * 0.6) + (Sharpe Ratio * 10) - (Expense Ratio * 5)
# This rewards high returns and high Sharpe, while penalizing high expense ratios
df['risk_adjusted_score'] = (df['returns_3yr'] * 0.6) + (df['sharpe'] * 10) - (df['expense_ratio'] * 5)

# 6. Filter for the "Top 30 Low-Risk, High-Return Funds"
# Criteria: Positive Sharpe ratio, at least 3 years of age, and high risk-adjusted score
top_funds = df[
    (df['sharpe'] > 0) & 
    (df['fund_age_yr'] >= 3) & 
    (df['category'] == 'Equity') # Focus on equity for growth demonstration
].nlargest(30, 'risk_adjusted_score')

# 7. Save the cleaned datasets
df.to_csv('cleaned_all_funds.csv', index=False)
top_funds.to_csv('top_30_mutual_funds.csv', index=False)

print("Data cleaning complete!")
print(f"Original rows: {len(df)}")
print(f"Top 30 funds saved successfully.")