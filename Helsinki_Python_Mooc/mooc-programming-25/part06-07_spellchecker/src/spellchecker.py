# write your solution here

acceptable_words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        acceptable_words.append(line)

new_string = ""
user_input = input(f"Write text: ")
user_input_as_list_of_words = user_input.split()
for word in user_input_as_list_of_words:
    word_lower = word.lower()
    if len(new_string) > 0:
        new_string += " "
    if word_lower in acceptable_words:
        new_string += word
    else:
        new_string += ("*" + word + "*")

print(new_string)
