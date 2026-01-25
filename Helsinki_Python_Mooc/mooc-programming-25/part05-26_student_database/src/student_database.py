# Write your solution here
from statistics import mean

def add_student(list_of_students: dict, student_name):
    list_of_students[student_name] = {}

def add_course(list_of_students: dict, student_name, course):
    courses = list_of_students[student_name]
    new_course_name, new_course_grade = course
    
    # Find existing course and update grade if higher
    for course_name in courses: 
        if course_name == new_course_name:
            if new_course_grade > courses[course_name]:
                courses[course_name] = new_course_grade  
            return
    if new_course_name not in courses:
        if new_course_grade > 0:
            courses[new_course_name] = new_course_grade
    

def print_student(list_of_students: dict, student_name): 
    if student_name in list_of_students:
        courses = list_of_students[student_name]
        print(f"{student_name}:")
        if not courses: 
            print(" no completed courses")
        else:
            total = sum(courses.values())  
            print(f" {len(courses)} completed courses:")
            for course_name, grade in courses.items():  
                print(f"  {course_name} {grade}")
            average = total / len(courses)
            print(f" average grade {average}")
    else:
        print(f"{student_name}: no such person in the database")

def summary(students):
    print(f"students {len(students)}")

    course_counts = {student: len(courses) for student, courses in students.items()}
    print(f"most courses completed {course_counts[max(course_counts)]} {max(course_counts)}")
    
    average_grades = {student: mean(courses.values()) for student, courses in students.items()}    
    best_student = max(average_grades, key=average_grades.get)  
    print(f"best average grade {average_grades[best_student]:.1f} {best_student}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
