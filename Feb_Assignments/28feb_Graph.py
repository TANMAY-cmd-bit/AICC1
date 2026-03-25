import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
df["Grade"] = df["Marks"].apply(get_grade)
grade_counts = df["Grade"].value_counts()
plt.figure()
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
plt.title("Grade Distribution")
plt.show()
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()