# write your solution here
student_information = input("Student information: ")
exercises_completed = input("Exercises completed: ")

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

for student in students:
    print(f"{student["first"]} {student["last"]} {(sum(student["exercises"]))}")
    


