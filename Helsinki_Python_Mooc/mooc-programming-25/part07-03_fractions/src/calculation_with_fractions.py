# Write your solution here
def fractionate(amount: int):
    from fractions import Fraction
    f = []
    for i in range(amount):
        f.append(Fraction(1, amount))
    return f


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))
