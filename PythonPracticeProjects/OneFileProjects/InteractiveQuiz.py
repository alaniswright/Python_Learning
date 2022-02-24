#python InteractiveQuiz.py

turns = 0
score = 0

print(" ")
print("The quiz of A loves L. By A.")
print(" ")
questions = [
    {
        "Question" : "Where was A & L's first date? Was it A: The Rose & Crown,B: Clissold Park Tavern or C: Hare & Hounds",
        "Answer" : "A"
    },
    {
        "Question" : "On what date did A & L first make lurve? Was it A : First date, B: Third date, C: never - he's a virgin",
        "Answer" : "A"
    },
    {
        "Question" : "What's the minimum number of rooms A & L's next house will have? A: 3, B: 4, C: 5",
        "Answer" : "B"
    },
    {
        "Question" : "What do Lorraine & the cats not have in common? A: Love of blankets, B: Love of A, C: Furry bodies",
        "Answer" : "C"
    },
    {
        "Question" : "What will arrive at the house in 15 weeks time? A: Sauna, B: Hot Tub, C: New TV",
        "Answer" : "A"
    },
    {
        "Question" : "Who is Alan's favourite girlfriend ever? Was it A : Cat, B: Natalie, C: La Pluis",
        "Answer" : "C"
    }
]


#print(questions[0].get("Question"))

for list in questions:
    while True:
        print(list.get("Question"))
        user_answer = input("Pick A, B or C > ")
        actual_answer = list.get("Answer")
        wrong_answers = ["A", "B", "C"]
        wrong_answers.remove(actual_answer)

        if actual_answer == user_answer:
            score += 1
            turns += 1
            print(f"Correct! That's {score} out of {turns}")
            print(" ")
            break
        elif wrong_answers[0] == user_answer or wrong_answers[1] == user_answer:
            turns += 1
            print(f"You got it wrong. That's {score} out of {turns}")
            print(" ")
            break
        else:
            print("Invalid answer. Enter A, B or C")
            continue

print(f"CONGRATULATIONS! You have the winning score!")
print("Your prize is one sex voucher to use on your boyfriend within the next 5 minutes :)")
print(" ")
