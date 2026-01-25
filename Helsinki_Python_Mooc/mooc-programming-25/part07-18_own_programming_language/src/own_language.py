# Write your solution here
variables = {letter: 0 for letter in string.ascii_uppercase}

def run(program: list):
    for command in program:
        c = command.split(" ")
        if c[0] == "PRINT":
            print(str(c[1]))
        elif c[0] == "END":
            break

if __name__ == "__main__":
    program1 = []
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)