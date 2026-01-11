import random

swiss_grades = [1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6]
german_grades = [6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1]
american_grades = [
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "B",
    "B",
    "B",
    "B",
    "C",
    "F",
]
french_grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def grademaker():
    s1 = input("What grading System would you like to use? ")
    if s1 == 1:
        print("Swiss System")
        print("This is the Grade of your Student:")
        grade_random = random(swiss_grades)
        print(grade_random)


grademaker()
