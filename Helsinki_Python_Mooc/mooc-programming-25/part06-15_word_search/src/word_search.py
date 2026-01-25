# Write your solution here
def find_words(search_term: str):
    import string
    
    words = []
    matching_words = []

    with open("words.txt") as my_file:
        for line in my_file:
            words.append(line.strip())
    
    if "." in search_term:
        dict_of_letters = {}
        for i in range(len(search_term)):
            if search_term[i] in string.ascii_lowercase:
                dict_of_letters[i] = search_term[i]
        temporary_word_list = words.copy()
        for word in words:
            if len(word) != len(search_term):
                temporary_word_list.remove(word)
                continue
            for i in dict_of_letters.keys():
                if dict_of_letters[i] != word[i]:
                    try:
                        temporary_word_list.remove(word)
                    except:
                        continue
        matching_words = temporary_word_list
        

                
            


    elif search_term[0] == "*":
        for word in words:
            if word.endswith(search_term[1:]):
                matching_words.append(word)
    
    elif search_term[-1] == "*":
        for word in words:
            if word.startswith(search_term[0:-1]):
                matching_words.append(word)

    elif search_term in words:
        matching_words.append(search_term)

    return matching_words
    


if __name__ == "__main__":
    print(find_words("ca."))
    print(find_words("zoologic"))
    print(find_words("zdfgggbf"))
    print(find_words("*vokes"))
    print(find_words("reson*"))
    
    # ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']

