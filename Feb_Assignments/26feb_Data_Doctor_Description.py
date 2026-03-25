import pandas as pd
df = pd.read_csv("data.csv")
df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna("Unknown", inplace=True)
df.drop_duplicates(inplace=True)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower().str.strip()
print("\n--- Cleaned Dataset ---")
print(df.head())