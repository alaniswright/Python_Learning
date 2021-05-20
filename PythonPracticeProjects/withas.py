questions = {}

with open('QuizQuestions.txt', 'r') as file:
    for line in file:
        key, value = line.split("/")
        questions[key] = value

print(questions)
