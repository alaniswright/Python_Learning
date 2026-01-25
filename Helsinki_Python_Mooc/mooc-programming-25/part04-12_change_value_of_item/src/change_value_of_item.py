# Write your solution here
l = [1, 2, 3, 4, 5]

while True:
    position = int(input("Index: "))
    if position == -1:
        break
    value = int(input("New value: "))
    l[position] = value
    print(l)