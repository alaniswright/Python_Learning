# Write your solution here
while True: 
    number = 3 # int(input("Please type in a number: "))
    if number <= 0:
        break
    factorial = 1
    i = 1
    while i < number:
        i += 1
        factorial *= i
    print(f"The factorial of the number {number} is {factorial}") 
print("Thanks and bye!")