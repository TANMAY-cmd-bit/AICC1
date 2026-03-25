from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
messages = [
    "Win money now",
    "Free offer just for you",
    "Call me tomorrow",
    "Let's meet for lunch",
    "Congratulations you won a prize",
    "Important meeting at 10am"
]
labels = ["spam", "spam", "ham", "ham", "spam", "ham"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)
model = MultinomialNB()
model.fit(X, labels)
new_message = input("Enter a message: ")
new_data = vectorizer.transform([new_message])
prediction = model.predict(new_data)
print("Prediction:", prediction[0])