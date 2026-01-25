# Write your solution here
def length_of_longest(my_list: list):
    longest = 0
    for i in my_list:
        if len(i) > longest:
            longest = len(i)
    return longest
