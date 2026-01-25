# Write your solution here
def most_common_character(my_string: str):
    chars = {}
    for char in my_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    longest = []
    for char in chars:
        if chars[char] == max(chars.values()):
            longest.append(char)
    if len(longest) == 1:
        return longest[0]
    for char in my_string:
        if char in longest:
            return char
