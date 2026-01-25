def final_points():
    from datetime import datetime, time
    students = []
    with open("start_times.csv") as my_file:
        for line in my_file:
            line = line.strip()
            parts = line.split(";")
            t = datetime.strptime(parts[1], "%H:%M").time()
            s = t.hour * 60 + t.minute
            student = {
                "name": parts[0],
                "start time": s,
                "task": {}
            }
            students.append(student)

    with open("submissions.csv") as my_file:
        for line in my_file:
            line = line.strip()
            parts = line.split(";")
            t = datetime.strptime(parts[3], "%H:%M").time()
            s = t.hour * 60 + t.minute
            student_task = int(parts[1])
            student_task_score = int(parts[2])
            for student in students:
                if student['name'] == parts[0]:
                    # task and points
                    if s - student['start time'] > 180:
                        continue
                    elif student_task in student['task']:
                        if student_task_score > student['task'][student_task]:
                            student['task'][student_task] = student_task_score
                    else:
                        student['task'][student_task] = student_task_score

                    #end time
                    if 'end time' in student.keys():
                        if s > student['end time']:
                            student['end time'] = s
                    else:
                        student['end time'] = s
    
    
    d = {}
    for student in students:
        d.update({student['name']: sum(student['task'].values())})
    return d

if __name__ == "__main__":
    final_points()