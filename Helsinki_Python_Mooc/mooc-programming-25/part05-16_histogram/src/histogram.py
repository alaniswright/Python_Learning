# Write your solution here
from collections import Counter


def histogram(word: str):
    d = Counter(word)
    for k, v in d.items():
        print(f"{k} {v * "*"}")



if __name__ == "__main__":
    histogram("abba")