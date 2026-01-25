def generate_password(length_of_password):
    import random
    import string
    pw = random.choices(string.ascii_lowercase, k=length_of_password)
    return ''.join(pw)

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))