# Write your solution here
def line(i, s):
    if s == "":
        s = "*"
    print(i * s[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")