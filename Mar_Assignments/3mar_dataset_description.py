import pandas as pd
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90]
}
df = pd.DataFrame(data)
print("\n--- Dataset ---")
print(df)
X = df[["StudyHours"]]
y = df["Marks"]
print("\nFeature (Study Hours):")
print(X)
print("\nLabel (Marks):")
print(y)