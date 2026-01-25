# Write your solution here
import re

def filter_solutions():
    correct = ""
    incorrect = ""

    with open("solutions.csv") as my_file:
        for line in my_file:
            l = str(line).split(";")
            match = re.match(r'([0-9]+)([+\-*/])([0-9]+)', l[1].strip())
            num1, operand, num2 = match.groups()
            num1 = int(num1)
            num2 = int(num2)
            if operand == "-":
                result = num1 - num2
            if operand == "+":
                result = num1 + num2
            if result == int(l[2]):
                correct += line
            else:
                incorrect += line

    with open("correct.csv", "w") as my_file:
        my_file.write(correct)
    
    with open("incorrect.csv", "w") as my_file:
        my_file.write(incorrect)

if __name__ == "__main__":

    filter_solutions()