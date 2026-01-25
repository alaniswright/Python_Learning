# Write your solution here
def longest_series_of_neighbours(my_list: list):
    consecutive = [[] for i in range(len(my_list))]
    counter = 0
    for i in range(len(my_list)):
        if consecutive[0] == False:
            consecutive[counter].append(my_list[i])
        elif -1 <= (my_list[i] - my_list[i-1]) <= 1:
            consecutive[counter].append(my_list[i])
        else:
            counter += 1
            consecutive[counter].append(my_list[i])
    longest_sublist = [0, ""]
    for sublist in consecutive:
        if len(sublist) > longest_sublist[0]:
            longest_sublist[0] = len(sublist)
            longest_sublist[1] = sublist
    return longest_sublist[0]



if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))