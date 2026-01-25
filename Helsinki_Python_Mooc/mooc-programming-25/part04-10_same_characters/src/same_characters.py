def same_chars(words: str, num1: int, num2: int):
    if (len(words) - 1) <= num1 or (len(words)-1) <= num2:
        return False
    elif words[num1] == words[num2]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False