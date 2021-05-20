#python ex39a_dictionaries.py

nation = {
    'EN': 'England',
    'SC': 'Scotland',
    'WA': 'Wales',
    'NI': 'Northern Ireland'
}

city = {
    'England': 'London',
    'Wales': 'Cardiff',
    'SC': 'Edinburgh',
    'NI': 'Belfast'
}

def divider():
    print('-' * 10)

print("Accessing a dictionary item:")
print(nation['EN'])
print(nation.get('EN')) # get is another way of accessing a list item
print(city[nation['EN']])
divider()

print("All the keys in the dictionary are: ", nation.keys())
print("All the values in the dictionary are: ", nation.values())
divider()

if 'EN' in nation:
    print("Yes, 'EN' is a key in this dictionary")
divider()

# changing items
nation["WA"] = "Cymru"
print(nation["WA"])
divider()

# adding items
nation["IR"] = "Ireland"
print(nation['IR'])
divider()

# removing items
print(f"Removing ", {nation.pop("IR")})
print(nation)
divider()

# looping through
for x in nation:
    print(x)
for x in nation.keys():
    print(x)
for x in nation.values():
    print(x)
for x, y in nation.items():
    print(x, y)
divider()

# Copying
new_nations = nation.copy()
print(new_nations)
divider()

# clear()
new_nations.clear()
print(new_nations)

# fromkeys() - The fromkeys() method returns a dictionary with the specified keys and the specified value.

# popitem() - Returns most recently added item

# setdefault()
