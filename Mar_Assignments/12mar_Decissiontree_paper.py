from sklearn.tree import DecisionTreeClassifier
X = [
    [0, 0, 0],  # Sunny, High, No
    [0, 1, 0],  # Sunny, Normal, No
    [1, 0, 1],  # Rainy, High, Yes
    [1, 1, 0],  # Rainy, Normal, No
]
y = [0, 1, 0, 1]
model = DecisionTreeClassifier()
model.fit(X, y)
prediction = model.predict([[0, 1, 0]])
if prediction[0] == 1:
    print("Play Outside ✅")
else:
    print("Do Not Play ❌")