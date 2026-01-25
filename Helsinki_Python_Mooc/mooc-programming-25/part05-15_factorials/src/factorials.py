# Write your solution here
def factorials(n: int):
    dictionary = {}
    for i in range(1, n+1):
        j = 1
        for k in range(1, i+1):
            j *= k
        dictionary[i] = j
    return dictionary

