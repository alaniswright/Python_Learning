# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    total = 0
    for i in my_matrix:
        for l in i:
            if l == element:
                total += 1
    return total
