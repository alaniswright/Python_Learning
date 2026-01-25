# write your solution here
student_information = input("Student information: ")
exercises_completed = input("Exercises completed: ")
exam_points = input("Exam points: ")

students = []
with open(student_information) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students.append({
            "id": parts[0],
            "first": parts[1],
            "last": parts[2]
        })

exercises_dict = {}
with open(exercises_completed) as new_file:
    for line in new_file:
        line = line.strip("\n")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises_dict[parts[0]] = [int(x) for x in parts[1:]]

for student in students:
    student["exercises"] = exercises_dict.get(student["id"], [])

exampoints_dict = {}
with open(exam_points) as new_file:
    for line in new_file:
        line = line.strip("\n")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exampoints_dict[parts[0]] = [int(x) for x in parts[1:]]

for student in students:
    student["exam_points"] = exampoints_dict.get(student["id"], [])

for student in students:
    student["total_points"] = sum(student["exam_points"]) + (sum(student["exercises"]) // 4)
    grade = 5
    if student["total_points"] < 28:
        grade = 4
    if student["total_points"] < 24:
        grade = 3
    if student["total_points"] < 21:
        grade = 2
    if student["total_points"] < 18:
        grade = 1
    if student["total_points"] < 15:
        grade = 0
    student["grade"] = grade

for student in students:
    print(f"{student["first"]} {student["last"]} {(student["grade"])}")

    


