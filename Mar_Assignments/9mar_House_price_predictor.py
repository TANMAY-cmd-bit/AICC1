import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Area": [500, 800, 1000, 1200, 1500, 1800],
    "Price": [1000000, 1500000, 2000000, 2400000, 3000000, 3600000]
}
df = pd.DataFrame(data)
X = df[["Area"]]
y = df["Price"]
model = LinearRegression()
model.fit(X, y)
area = float(input("Enter house area: "))
predicted_price = model.predict([[area]])
print("Predicted House Price:", int(predicted_price[0]))