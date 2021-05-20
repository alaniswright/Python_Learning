
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(F"There are {len(stuff)} items now.")

print("THere we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #Prints 2nd item in list (cardinal 1st)
print(stuff[-1]) #Prints last item in list
print(stuff.pop()) #Removes last item from list and returns removed items
print(' '.join(stuff)) #Joins elements of the list together separated by ' '
print('#'.join(stuff[3:5])) #Combines the 3rd and 4th element of the list, separating them with a '#'
