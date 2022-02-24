#python InchesCmConverter.py

inches_to_cm = 2.54
cm_to_inches = 0.393701

while True:
    choice = input("inches or cm?")
    if choice == "cm":
        print(f"1 cm is the same as {cm_to_inches}inches")
        break
    elif choice == "inches":
        print(f"1 inch is the same as {inches_to_cm}cm")
        break
    else:
        print("You need to write inches or cm")
        continue
