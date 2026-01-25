# Write your solution here
l = []
while True:
    print(f"The list is now {l}")
    user_decision = input("a(d)d, (r)emove or e(x)it: ")
    if user_decision == "d":
        if l:
            l.append(max(l) + 1)
        else:
            l.append(1)
    elif user_decision == "r":
        l.pop(-1)
    elif user_decision == "x":
        break
print("Bye!")