# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        new_dict = {}
        for line in new_file:
            chunk = line.split(";")
            new_dict[chunk[0]] = float(chunk[1])
        return new_dict