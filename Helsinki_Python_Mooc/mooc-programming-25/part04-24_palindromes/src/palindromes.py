# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word):
    halfway = int(len(word) / 2) + len(word) % 2
    first_half = word[0:halfway]
    second_half = word[-1:-halfway-1:-1]
    if first_half == second_half:
        return True
    else:
        return False

while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input) == True:
        print(f"{user_input} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# if __name__ == "__main__":

