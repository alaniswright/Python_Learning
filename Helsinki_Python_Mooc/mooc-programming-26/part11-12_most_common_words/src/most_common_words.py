# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as my_file:
        words = [''.join([char for char in word if char.isalnum()]) for line in my_file for word in line.split(" ")]
        
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))