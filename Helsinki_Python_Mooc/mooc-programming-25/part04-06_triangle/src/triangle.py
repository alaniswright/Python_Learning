# Copy here code of line function from previous exercise
def line(i, s):
    if s == "":
        s = "*"
    print(i * s[0])

def triangle(size):
    x = 1
    while x <= size:
        line(x, "#")
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
