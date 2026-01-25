from collections import Counter
# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
      count_of_nums = Counter(my_list)
      return count_of_nums.most_common(1)[0][0]

    @classmethod
    def doubles(cls, my_list: list):
      count_of_nums = Counter(my_list)
      appear_twice = [v for k, v in count_of_nums.items() if v >= 2]
      return len(appear_twice)

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))