# Write your solution here
def new_person(name: str, age: int):
    if len(name) > 40 or name == "" or len(name.split()) < 2:
        raise ValueError(f"{name} input is invalid")
    elif age < 0 or age > 150:
        raise ValueError(f"{age} input is invalid")
    return (name, age)
if __name__ == "__main__":
    print(new_person("Alan", 40))
    print(new_person('Tim Andrew Smith', 97))