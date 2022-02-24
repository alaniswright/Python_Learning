import datetime

def enter_date():
    while True:
        try:
            date = input("Enter data in format yyyy-mm-dd: ")
            year,month,day = date.split("-")
            return datetime.date(int(year), int(month), int(day))
        except ValueError:
            print("Incorrect date format. Try again")
            #raise ValueError("Incorrect date format. Try again")
            continue

dateA = enter_date()
dateB = enter_date()

print(f"The time difference between {dateA} and {dateB} is {abs(dateA - dateB)}")
