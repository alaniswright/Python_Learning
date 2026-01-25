# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.total += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        if self.numbers > 0:
            return self.total
        else:
            return 0

    def average(self):
        if self.numbers > 0:
            return self.total / self.numbers
        else:
            return 0

def number_collection():
    num = NumberStats()
    evens = NumberStats()
    odds = NumberStats()
    while True:
        value = int(input("Please type in integer numbers: "))
        if value == -1:
            break
        else:
            num.add_number(value)
        if value % 2 == 0:
            evens.add_number(value)
        elif value % 2 == 1:
            odds.add_number(value)
    print(f"Sum of numbers: {num.get_sum()}")
    print(f"Mean of numbers: {num.average()}")
    print(f"Sum of even numbers: {evens.get_sum()}")
    print(f"Sum of odd numbers: {odds.get_sum()}")

number_collection()