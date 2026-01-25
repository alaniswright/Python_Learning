# Write your solution here
def list_sum(l1: list, l2: list):
    new_list = []
    for i in range(len(l1)):
        new_list.append(l1[i] + l2[i])
    return new_list
