# write your solution here
def matrix():
    with open("matrix.txt") as new_file:
        row_sums = []
        largest_value = 0
        for line in new_file:
            this_row_sum = 0
            row_of_values = line.split(",")
            for value in row_of_values:
                v = int(value)
                this_row_sum += v
                if v > largest_value:
                    largest_value = v
            row_sums.append(this_row_sum)
        return [row_sums, largest_value]

def matrix_sum():
    row_sums, largest_value = matrix()
    total = 0
    for r in row_sums:
        total += r
    return total


def matrix_max():
    row_sums, largest_value = matrix()
    return largest_value

def row_sums():
    row_sums, largest_value = matrix()
    return row_sums
