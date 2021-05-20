start = int(input("start: "))
upper = int(input("upper: "))
increment = int(input("increment: "))
numbers = []

def loop(start, upper):
    for i in range(start,upper):
        print(f"At the top i is {start}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {start}")

loop(start, upper)

print("The numbers: ")

for num in numbers:
    print(num)
