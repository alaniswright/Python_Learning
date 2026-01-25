def cheaters():
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
                "start time": s
            }
            students.append(student)

    with open("submissions.csv") as my_file:
        for line in my_file:
            line = line.strip()
            parts = line.split(";")
            t = datetime.strptime(parts[3], "%H:%M").time()
            s = t.hour * 60 + t.minute
            for student in students:
                if student['name'] == parts[0]:
                    student['task'] = int(parts[1])
                    student['points'] = int(parts[2])
                    if 'end time' in student.keys():
                        if s > student['end time']:
                            student['end time'] = s
                    else:
                        student['end time'] = s

    cheaters = []
    
    for student in students:
        if student['end time'] - student['start time'] > 180:
            cheaters.append(student['name'])
     
    return cheaters

if __name__ == "__main__":
    cheaters()