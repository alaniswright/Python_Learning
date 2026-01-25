# Write your solution here
def read_input(message: str, num1: int, num2: int):
    while True:
        try:
            user_input = int(input(f"{message}"))
            if num1 <= user_input <= num2:
                return user_input
        except:
            pass
        print(f"You must type in an integer between {num1} and {num2}")
        

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)