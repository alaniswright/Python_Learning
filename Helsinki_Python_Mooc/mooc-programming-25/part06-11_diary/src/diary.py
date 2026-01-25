# Write your solution here
with open("diary.txt") as my_file:
    current_diary = ""
    for line in my_file:
        current_diary += str(line)


while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        if current_diary != "":
            print("Entries: ")
            print(current_diary)
        diary_entry = input("Diary entry: ")
        current_diary += str(diary_entry + "\n")
        print("Diary saved")
        print()
    if function == 2:
        print("Entries: ")
        print(current_diary)
    if function == 0:
        print("Bye now!")
        break

with open("diary.txt", "w") as my_file:
    my_file.write(current_diary + "\n")