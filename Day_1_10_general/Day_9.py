student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}


def give_grade(score: int) -> str:
    if score < 71:
        return "Fail"
    elif score < 81:
        return "Acceptable"
    elif score < 91:
        return "Exceeds Expectations"
    else:
        return "Outstanding"


for student in student_scores:
    student_grades[student] = give_grade(student_scores[student])

print(student_grades)
