# Write your solution here
def oldest_person(people: list):
    oldest = 0
    oldest_person = ""
    for p in people:
        if (2025 - p[1]) > oldest:
            oldest = 2025 - p[1]
            oldest_person = p[0]
    return oldest_person



