import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = {
    "Annual_Income": [15, 16, 17, 18, 30, 35, 40, 45, 60, 65, 70, 75],
    "Spending_Score": [39, 81, 6, 77, 40, 60, 50, 70, 20, 30, 90, 85]
}
df = pd.DataFrame(data)
X = df[["Annual_Income", "Spending_Score"]]
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)
plt.figure()
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
print(df)