# Write your solution here
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
import datetime
birthday = datetime.datetime(year, month, day)
millenium = datetime.datetime(1999, 12, 31)
if birthday < millenium:
    age = (millenium - birthday).days
    print(f"You were {age} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")

