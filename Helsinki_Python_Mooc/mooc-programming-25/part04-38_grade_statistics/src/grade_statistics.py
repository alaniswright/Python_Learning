# Write your solution here
scores = []

while True:
    submission = input("Exam points and exercises completed: ")
    if submission == "":
        break
    score = submission.split(" ")
    score[0] = int(score[0])
    score[1] = int(int(score[1]) * 0.1)
    scores.append([score[0], score[0] + score[1]])

grades = [0,0,0,0,0,0] # Grades 0,1,2,3,4,5 - same as indexes

students_total = len(scores)

points_total = 0

for pair in scores:
    if pair[0] < 10:
        grades[0] += 1
    elif pair[1] <= 14:
        grades[0] += 1
    elif pair[1] <= 17:
        grades[1] += 1
    elif pair[1] <= 20:
        grades[2] += 1
    elif pair[1] <= 23:
        grades[3] += 1
    elif pair[1] <= 27:
        grades[4] += 1
    elif pair[1] <= 30:
        grades[5] += 1
    points_total += pair[1]
    
points_average = points_total / students_total

pass_percentage = 100 * (sum(grades) - grades[0]) / sum(grades)

print(f"""
Statistics: 
Points average: {round(points_average, 1)}
Pass percentage: {round(pass_percentage, 1)}
Grade distribution:
  5: {grades[5] * "*"}
  4: {grades[4] * "*"}
  3: {grades[3] * "*"}
  2: {grades[2] * "*"}
  1: {grades[1] * "*"}
  0: {grades[0] * "*"}
""")

