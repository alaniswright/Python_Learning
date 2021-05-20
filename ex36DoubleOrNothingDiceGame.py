import random

balance = 100
target = 200

def name():
    name = input("Your name: ")
    return name

def age(name):
    age = int(input("Your age: "))
    if age < 18:
        print(f"Sorry {name}. You are too young to play!")
        exit()

def pick_number():
    while True:
        try:
            selection = int(input("Pick a number between 1 and 6: "))
            if 6 >= selection > 1:
                print(f"You picked {selection}")
                return selection
                break
            else:
                print("Wrong. Pick a number between 1 and 6")
        except:
            print("Provide an integar value")
            continue

def play_game(balance):
    dice = random.randint(1, 6)
    print(f"The dice rolled a {dice}. And the number you picked was {selection}")
    if dice == selection:
        print("Congratulations! You got it right!")
        balance += 50
        print(f"{balance} is your new balance.")
        return balance
    else:
        print("Sorry, you got it wrong :(")
        balance -= 50
        print(f"{balance} is your new balance.")
        return balance



name()
age(name)
while True:
    selection = pick_number()
    balance = play_game(balance)
    if balance == 0:
        print("Your balance is 0. You lose!")
        break
    elif balance == 200:
        print("Your balance is 200. You win!")
        break
