# Write your solution here
def no_shouting(my_list: list):
    new_list = [word for word in my_list if word.isupper() == False]
    return new_list