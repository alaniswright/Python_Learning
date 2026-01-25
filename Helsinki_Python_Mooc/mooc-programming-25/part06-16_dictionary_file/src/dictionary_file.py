# Write your solution here
d = {}

with open("dictionary.txt") as my_file:
    try:
        for line in my_file:
            line = line.split(":")
            d[line[0]] = line[1]
    except:
        pass


while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    
    if function == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        if finnish not in d:
            d[finnish] = english
            print("Dictionary entry added")
            with open("dictionary.txt", "a") as my_file:
                my_file.write(f"{finnish}:{english}\n")
    
    elif function == 2:
        search_term = input("Search term: ")
        for word in d.values():
            if search_term in word:
                key_of_search_term = [key for key, value in d.items() if value == word]
                print(f"{key_of_search_term[0]} - {word}")
        else:
            for word in d.keys():
                if search_term in word:
                    print(f"{word} - {d[word]}")
    
    elif function == 3:
        print("Bye!")
        break
