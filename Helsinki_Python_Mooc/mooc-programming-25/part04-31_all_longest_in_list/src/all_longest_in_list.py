# Write your solution here
def all_the_longest(my_list: list):
    lengths = [len(i) for i in my_list]
    longest = max(lengths)
    longest_words = []
    for word in my_list:
        if len(word) == longest:
            longest_words.append(word)
    return longest_words

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']