# Write your solution here
def separate_characters(my_string: str):
    import string

    new_string = ["","",""]

    for letter in my_string:
        if letter in string.ascii_letters:
            new_string[0] += letter
        elif letter in string.punctuation:
            new_string[1] += letter
        else:
            new_string[2] += letter
    
    return tuple(new_string)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])