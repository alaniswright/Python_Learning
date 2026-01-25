# Write your solution here
def  roll(die: str):
    import random
    if die == "A":
        die = [3, 3, 3, 3, 3, 6]
    if die == "B":
        die = [2, 2, 2, 5, 5, 5]
    if die == "C":
        die = [1, 4, 4, 4, 4, 4]
    selection = random.sample(die, 1)
    return selection[0]

def play(die1: str, die2: str, times: int):
    counter = 0
    score = [0,0,0]
    while counter < times:
        d1 = roll(die1)
        d2 = roll(die2)
        if d1 > d2:
            score[0] += 1
        elif d1 < d2:
            score[1] += 1
        elif d1 == d2:
            score[2] += 1
        counter += 1
    return tuple(score)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    play("A", "B", 10)