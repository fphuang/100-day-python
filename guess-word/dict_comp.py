names = ["Alex", "Angela", "Dave", "Eileen", "Fangping"]

import random

# student_scores = {student: random.randint(0, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)


import pandas as pd


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

df = pd.DataFrame(student_dict)

for (index, row) in df.iterrows():
    # print(index)
    print(row.scores)
