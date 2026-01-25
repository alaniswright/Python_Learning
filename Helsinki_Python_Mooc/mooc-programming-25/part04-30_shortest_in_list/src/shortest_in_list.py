# Write your solution here
def shortest(my_list: list):
    lengths = [len(i) for i in my_list]
    minimum_value = min(lengths)
    minimum = lengths.index(minimum_value)
    return my_list[minimum]
