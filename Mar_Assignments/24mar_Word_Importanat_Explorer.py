from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
documents = [
    "Machine learning is very useful in data science",
    "Python is widely used for machine learning",
    "Data science includes machine learning and statistics",
    "Artificial intelligence and machine learning are related",
    "Python is great for data analysis"
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print("\n--- TF-IDF Matrix ---")
print(df)
print("\n--- Top Keywords ---")
for i, row in df.iterrows():
    top_words = row.sort_values(ascending=False).head(3)
    print(f"Document {i+1}: {list(top_words.index)}")