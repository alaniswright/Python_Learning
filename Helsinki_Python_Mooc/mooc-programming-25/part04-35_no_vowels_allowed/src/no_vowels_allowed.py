# Write your solution here
def no_vowels(my_string: str):
    new_string = ""
    vowels = "aeiou"
    for char in my_string:
        if char not in vowels:
            new_string += char
    return new_string
    