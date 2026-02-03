"""
TODO:
Dictionary of students -> grades
Print averages
"""
students = {"student": {"name": "Abby", "ID": 123, "Grade": 87},
           "student2": {"name": "Hannah", "ID": 456, "Grade": 99},
           "student3": {"name": "Avigayil", "ID": 789, "Grade": 72}
           }
sum = 0
for key in students:
    info = students[key]
    sum += info["Grade"]
print(sum/len(students))