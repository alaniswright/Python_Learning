from sys import argv
script, firstname = argv

surname = input("Surname: ")

print(f"{firstname} {surname}")
print("This is a {} string".format("not so good way of inserting things into a "))
