def store_personal_data(person: tuple):
    my_csv_row = str(person[0]) + ";" + str(person[1]) + ";" + str(person[2])
    with open('people.csv','a') as my_file:
        my_file.write(my_csv_row)


