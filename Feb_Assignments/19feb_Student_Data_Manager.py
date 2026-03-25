students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
topper = max(students, key=students.get)
average = sum(students.values()) / len(students)
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
print("\n--- Student Results ---")
for name, marks in students.items():
    print(f"{name}: {marks} -> Grade {get_grade(marks)}")

print("\nTopper:", topper, "-", students[topper])
print("Class Average:", round(average, 2))