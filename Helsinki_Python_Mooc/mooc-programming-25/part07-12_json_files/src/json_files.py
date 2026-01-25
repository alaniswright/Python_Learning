# Write your solution here
def print_persons(filename: str):
    import json

    with open(filename) as my_file:
        data = my_file.read()

    courses = json.loads(data)
    for i in courses:
        print(f"{i['name']} {i['age']} years {str(i['hobbies']).replace("[", "(").replace("]", ")").replace("'", "")}")

if __name__ == "__main__":
    print_persons("file1.json")