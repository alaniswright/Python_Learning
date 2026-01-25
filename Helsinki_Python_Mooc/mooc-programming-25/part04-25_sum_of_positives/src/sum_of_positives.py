# Write your solution here
def sum_of_positives(l):
    total = 0
    for i in l:
        if i > 0:
            total += i
    return total