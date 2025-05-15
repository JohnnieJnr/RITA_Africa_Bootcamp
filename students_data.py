# Importing pandas with an alias
import pandas as pd

data = pd.read_csv("students.csv")

print("This is our existing students: \n", data)

name = input("Please enter a student name: ")
age = input("Please enter a student's age: ")
grade = input("Enter the student's grade: ").upper()

new_student = {
    "Name" : name,
    "Age" : age,
    "Grade" : grade,
}

new_df =pd.DataFrame([new_student])
updated_data = pd.concat([data, new_df],ignore_index=True)

updated_data.to_csv("students.csv", index = True)

print("\n Students added successfully")
print(updated_data)
