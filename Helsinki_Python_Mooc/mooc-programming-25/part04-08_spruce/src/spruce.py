# Write your solution here
def spruce(num):
    print("a spruce!")
    x = 1
    white_space = num - 1
    while white_space >= 0:
        print(f"{" " * white_space}{x * "*"}{" " * white_space}")
        white_space -= 1
        x += 2
    white_space = num - 1
    print(f"{" " * white_space}{"*"}{" " * white_space}")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)