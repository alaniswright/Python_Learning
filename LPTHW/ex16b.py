from sys import argv

script, filename = argv

target_file = open(filename, 'w')

new_text = input("This is my new text: ")
target_file.write(new_text)
