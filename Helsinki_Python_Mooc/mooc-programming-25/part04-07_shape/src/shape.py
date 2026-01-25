# Copy here code of line function from previous exercise and use it in your solution
# Copy here code of line function from previous exercise
def line(i, s):
    if s == "":
        s = "*"
    print(i * s[0])

def shape(tri_size, tri_char, squ_size, squ_char):
    x = 1
    while x <= tri_size:
        line(x, tri_char)
        x += 1
    x = 1
    while x <= squ_size:
    # You should call function line here with proper parameters
        line(tri_size, squ_char)
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")