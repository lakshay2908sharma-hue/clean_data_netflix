import pandas as pd
# Load dataset
df = pd.read_csv("netflix_data.csv")
# 1. Check data
print("Initial Info:\n", df.info())
print("\nMissing Values:\n", df.isnull().sum())
# 2. Handle missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna("Not Available")
# 3. Remove duplicates
df = df.drop_duplicates()
# 4. Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
# 5. Convert date column
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# 6. Standardize text
df['type'] = df['type'].str.lower()
df['country'] = df['country'].str.strip()
# 7. Check final data
print("\nAfter Cleaning:\n", df.isnull().sum())
# 8. Save cleaned dataset
df.to_csv("clean_data_netflix.csv", index=False)
print("\n✅ Data Cleaning Completed & File Saved!")