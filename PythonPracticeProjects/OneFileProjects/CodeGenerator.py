from string import ascii_letters, printable

users_word = input("Enter your word: ")
new_word_letters = ""
new_word_all_chars = ""
key = 5


for letter in users_word:
    if letter in ascii_letters:
        new_word_letters += ascii_letters[(ascii_letters.index(letter) + key) % (1 + len(ascii_letters))]
    else:
        new_word_letters += letter

for char in users_word:
    if char in printable:
        new_word_all_chars += printable[(printable.index(char) + key) % (len(printable) + 1)]
    else:
        new_word_all_chars += char

print("User's word is " + users_word)
print("Generating code in letters only...")
print("Your new word is: " + new_word_letters)
print("...")
print("Generating code using all possible ASCII characters...")
print("Your new word is: " + new_word_all_chars)
