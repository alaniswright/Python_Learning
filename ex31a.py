print("Pick a number from 1 to 6.")

number = input("> ")

if number == 1:
    print("You guessed correct!")
elif number == 2:
    print("Not quite, but close!")
else:
    print(f"Sorry, {number} is miles off.")
