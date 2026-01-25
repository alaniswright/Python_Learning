# Write your solution here
phonebook = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))
    if user_input == 3:
        break
    elif user_input == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in phonebook:
            phonebook[name] = [number]
        elif name in phonebook:
            phonebook[name].append(number)
        print("ok!")
    elif user_input == 1:
        name = input("name: ")
        if name in phonebook:
            for i in phonebook[name]:
                print(i)
        else:
            print("no number")
print("quitting...")