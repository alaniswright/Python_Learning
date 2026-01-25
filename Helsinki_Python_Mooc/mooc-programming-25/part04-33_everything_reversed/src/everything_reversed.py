# Write your solution here
def everything_reversed(my_list: list):
    new_list = []
    for word in my_list:
        new_list.append(word[::-1])
    return new_list[::-1]