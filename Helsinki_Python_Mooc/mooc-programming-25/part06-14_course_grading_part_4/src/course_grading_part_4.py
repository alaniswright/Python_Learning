# write your solution here
student_information = input("Student information: ")
exercises_completed = input("Exercises completed: ")
exam_points = input("Exam points: ")
course = input("Course: ")

"""student_information = "students1.csv" #input("Student information: ")
exercises_completed = "exercises1.csv" #input("Exercises completed: ")
exam_points = "exam_points1.csv" #input("Exam points: ")
course = "course1.txt" #input("Course: ")"""

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

n = "name"
"""print(f"{n:30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
for student in students:
    name = student["first"] + " " + student["last"]
    print(f"{name:30}{sum(student["exercises"]):<10}{sum(student["exercises"])//4:<10}{sum(student["exam_points"]):<10}{student["total_points"]:<10}{student["grade"]:<10}")"""

intro = ''
with open(course) as my_file:
    for line in my_file:
        line = line.strip().split(",")
        if intro == '':
            l = line[0].split(':')
            intro += l[1][1:]
        else:
            l = line[0].split(' ')
            intro += (", " + l[2] + " credits")

with open("results.txt", "w") as my_file:
    my_file.write(intro + "\n")
    my_file.write("======================================\n")
    my_file.write((f"{n:30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade"}\n"))
    for student in students:
        name = student["first"] + " " + student["last"]
        my_file.write(f"{name:30}{sum(student["exercises"]):<10}{sum(student["exercises"])//4:<10}{sum(student["exam_points"]):<10}{student["total_points"]:<10}{student["grade"]}\n")

with open("results.csv", "w") as my_file:
    for student in students:
        name = student["first"] + " " + student["last"]
        my_file.write(f"{student["id"]};{name};{student["grade"]}\n")

    


