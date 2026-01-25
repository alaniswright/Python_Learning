# Write your solution here
def even_numbers(l):
    evens = []
    for i in l:
        if i % 2 == 0:
            evens.append(i)
    return evens