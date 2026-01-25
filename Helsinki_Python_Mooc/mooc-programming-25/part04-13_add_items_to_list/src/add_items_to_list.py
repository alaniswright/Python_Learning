# Write your solution here
num_of_items = int(input("How many items: "))
i = 1
items = []
while i <= num_of_items:
    item = int(input(f"Item {i}: "))
    items.append(item)
    i += 1
print(items)