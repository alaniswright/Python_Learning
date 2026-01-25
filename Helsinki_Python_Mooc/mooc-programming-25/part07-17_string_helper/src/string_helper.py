# Write your solution here
import string

def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string

def split_in_half(orig_string: str):
    length = len(orig_string) // 2
    s = (orig_string[0:length], orig_string[length:])
    return s

def remove_special_characters(orig_string: str):
    allowed_characters = string.ascii_letters + string.digits + " "
    new_string = ""
    for char in orig_string:
        if char in allowed_characters:
            new_string += char
    return new_string

if __name__ == "__main__":
    print(change_case("ALan"))
    print(split_in_half("alana"))
    print(remove_special_characters("!Alan"))
