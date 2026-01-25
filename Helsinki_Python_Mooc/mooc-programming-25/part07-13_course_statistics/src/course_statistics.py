# Write your solution here
def retrieve_all():
    import urllib.request
    import json
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    courses = json.loads(my_request.read())
    
    active = []
    for i in courses:
        if i["enabled"] == True:
            entry = (i["fullName"], i["name"], i["year"], sum(i["exercises"]))
            active.append(entry)
    
    return active

def retrieve_course(course_name: str):
    import urllib.request
    import json

    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"

    my_request = urllib.request.urlopen(url)

    course = json.loads(my_request.read())

    print(course)

    d = {}
    d['weeks'] = len(course)

    students = 0
    hours = 0
    exercises = 0
    for k, v in course.items():
        if v['students'] > students:
            students = v['students']
        hours += v['hour_total']
        exercises += v['exercise_total']
        
    d['students'] = students
    d['hours'] = hours
    d['hours_average'] = int(hours / students)
    d['exercises'] = exercises
    d['exercises_average'] = int(exercises / students)

    return d


if __name__ == "__main__":
    #retrieve_all())
    print(retrieve_course("docker2019"))
