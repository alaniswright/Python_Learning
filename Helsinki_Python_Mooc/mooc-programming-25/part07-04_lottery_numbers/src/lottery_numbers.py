# Write your solution here
def lottery_numbers(amount: int, lower: int, upper: int):
    from random import randrange
    random_numbers = []
    i = 0
    while i < amount:
        random_numbers.append(randrange(lower, upper))
        i += 1
    random_numbers = sorted(random_numbers)
    return random_numbers


if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)