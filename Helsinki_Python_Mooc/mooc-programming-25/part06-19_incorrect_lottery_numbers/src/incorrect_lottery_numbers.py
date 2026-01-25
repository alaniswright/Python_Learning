# Write your solution here
def filter_incorrect():
    valid_weeks = [i for i in range(1,53)]
    valid_values = [i for i in range(1,40)]
    correct_list = []

    with open("lottery_numbers.csv") as my_file:
        for line in my_file:
            try:
                correct = True
                l = line.split(";")
                week = l[0].split(" ")
                values = l[1].split(",")
            
                for i in values:
                    try:
                        if int(week[1]) not in valid_weeks:
                            correct = False
                        elif len(values) != 7:
                            correct = False
                        elif int(i) == False:
                            correct = False
                        elif values.count(i) > 1:
                            correct = False
                        elif int(i) not in valid_values:
                            correct = False
                    except:
                        correct = False

                if correct == True:
                    correct_list.append(line)
                    """with open("correct_numbers.csv", "a") as new_file:
                        new_file.write(line)"""

            except:
                pass
        with open("correct_numbers.csv", "w") as new_file:
            for l in correct_list:
                new_file.write(l)

if __name__ == "__main__":
    filter_incorrect()