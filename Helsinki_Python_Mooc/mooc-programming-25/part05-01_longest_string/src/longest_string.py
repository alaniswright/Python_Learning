# Write your solution here
def longest(strings: list):
    longest_string_length = 0
    longest_string_name = ""
    for s in strings:
        if len(s) > longest_string_length:
            longest_string_name = s
            longest_string_length = len(s)
    return longest_string_name

if __name__ == "__main__":
    strings = ["first", "second", "third"]
    print(longest(strings))