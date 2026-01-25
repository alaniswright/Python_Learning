def generate_strong_password(length_of_password, include_numbers, include_special_chars):
    import random
    import string
    possible_characters_for_password = string.ascii_lowercase
    pw = random.choices(string.ascii_lowercase, k=1)
    if include_numbers == True:
        possible_characters_for_password += string.digits
        pw += random.choices(string.digits, k=1)
    if include_special_chars == True:
        possible_characters_for_password += "!?=+-()#"
        pw += random.choices("!?=+-()#", k=1)
    remaining_digits_to_generate = length_of_password - len(pw)
    pw += random.choices(possible_characters_for_password, k=remaining_digits_to_generate)
    return ''.join(pw)

if __name__ == "__main__":
    print(generate_strong_password(8, True, True))
    print(generate_strong_password(8, False, False))
    print(generate_strong_password(8, True, False))
    print(generate_strong_password(8, False, True))