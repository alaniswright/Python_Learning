# Write your solution here
def words(n: int, beginning: str):
    import random

    words = []
    
    with open("words.txt") as new_file:
        for line in new_file:
            line = line.strip()
            if line.startswith(beginning):
                words.append(line)
    
    selected_words = random.sample(words, n)

    return selected_words
    

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)