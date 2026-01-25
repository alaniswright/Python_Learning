# Copy here code of line function from previous exercise
def line(i, s):
    if s == "":
        s = "*"
    print(i * s[0])

def square_of_hashes(size):
    x = 0
    while x < size:
    # You should call function line here with proper parameters
        line(size, "#")
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
