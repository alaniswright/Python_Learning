# Write your solution here
my_file = input("Filename: ")
starting_date = input("Starting date: ")
how_many_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

from datetime import datetime, timedelta
current_date = datetime.strptime(starting_date, "%d.%m.%Y")
starting_date = current_date

counter_of_days = 0
records = {}
while counter_of_days < how_many_days:
    days_input = input(f"Screen time {current_date.strftime("%d.%m.%y")}: ")
    records[current_date.strftime("%d.%m.%Y")] = days_input.split(" ")
    current_date += timedelta(days=1)
    counter_of_days += 1
end_date = starting_date + timedelta(days=counter_of_days-1)
print(f"Data stored in file {my_file}")
#print(records)

total = 0
for day in records.values():
    for entry in day:  
        total += int(entry)

average = total / int(how_many_days)

#print(total)
#print(average)

with open(my_file, "w") as new_file:
    new_file.write(f"Time period: {starting_date.strftime("%d.%m.%Y")}-{end_date.strftime("%d.%m.%Y")}\n")
    new_file.write(f"Total minutes: {total}\n")
    new_file.write(f"Average minutes: {average}\n")
    for k, v in records.items():
        new_file.write(f"{k}: {str(v).replace(", ", "/").replace("[", "").replace("]", "").replace("'", "")}\n")

