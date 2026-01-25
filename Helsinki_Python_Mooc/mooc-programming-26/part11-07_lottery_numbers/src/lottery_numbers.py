# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_number: int, numbers: list):
        self.week_number = week_number
        self.numbers = numbers
    
    def number_of_hits(self, numbers: list):
        return len([x for x in self.numbers if x in numbers])
    
    def hits_in_place(self, numbers):
        return [num if num in self.numbers else -1 for num in numbers]

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))