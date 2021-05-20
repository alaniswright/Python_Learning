best_films = ["Star Wars", "The Patriot", "Matrix", "Avatar"]

print("This is my list of best films: ", best_films)
print("---")

print("Adding new film to the list.  The list is now: ")
best_films.append("Avengers Endgame")
print(best_films)
print("---")

print("This makes the list a bit more readable: ", " - ".join(best_films))
print("---")

print("The first film on the list is: ", best_films[0], " and the last film on the list is: ", best_films[-1])
print("---")

print(f"Remove {best_films.pop(0)} from the list. The list is now: ")
print(best_films)
print("---")

print(f"There are {len(best_films)} in the list.")
print("---")

best_films_copy = best_films.copy()
print(f"Now you see it: {best_films_copy}")
print(f"Now you don\'t! (because I cleared it): {best_films_copy.clear()}")
print("---")

best_films_copy = best_films
print(best_films)
print(best_films_copy)
print("Now we're going to combine this list with a copy of itself.")
best_films.extend(best_films_copy)
print(best_films)
print("---")

print("Count how many times the Matrix appears")
print(best_films.count("Matrix"))
#print(f"The Matrix is in the list {best_films.count("Matrix")} times.")
print("---")

print("Matrix first appears at position #", best_films.index("Matrix"))
print("---")

print("Adding 'The Wedding Singer' to the list at position 2...")
best_films.insert(1, "Wedding Singer")
print(best_films)
print("---")

print("Reverse the list:")
best_films.reverse()
print(best_films)
print("---")

print("Sort the list: ")
best_films.sort()
print(best_films)
