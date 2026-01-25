# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest_so_far = 0
        for line in new_file:
            line = line.replace("\n", "")
            if int(line) > largest_so_far:
                largest_so_far = int(line)
    return largest_so_far
