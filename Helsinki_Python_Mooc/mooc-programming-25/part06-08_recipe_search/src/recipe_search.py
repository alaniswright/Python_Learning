# Write your solution here

def extract_recipes(filename):
    list_of_lines = []
    
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            list_of_lines.append(line)

    from itertools import groupby
    recipes = [list(g) for k, g in groupby(list_of_lines, key=bool) if k]
    return recipes

def search_by_name(filename, search_term):
    recipes = extract_recipes(filename)
    found_recipes = []
    for recipe in recipes:
        if search_term.lower() in recipe[0].lower():
            found_recipes.append(recipe[0])
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = extract_recipes(filename)
    found_recipes = []
    for recipe in recipes:
        if prep_time > int(recipe[1]):
            found_recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = extract_recipes(filename)
    found_recipes = []
    for recipe in recipes:
        if ingredient in recipe:
            found_recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return found_recipes

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    print(found_recipes)
    found_recipes = search_by_time("recipes1.txt", 20)
    print(found_recipes)
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    print(found_recipes)

