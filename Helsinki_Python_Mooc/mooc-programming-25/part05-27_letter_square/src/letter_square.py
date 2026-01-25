# Write your solution here
import string 
  
uppercase_letters = string.ascii_uppercase 
layers = int(input("Layers: "))
grid_width = (layers * 2) - 1
letters = uppercase_letters[0:layers]
grid = [[" " for _ in range(grid_width)] for _ in range(grid_width)]
for x in range(grid_width):
    for y in range(grid_width):
        grid[x][y] = letters[max((abs(x + 1 - layers)), (abs(y + 1 - layers)))]
for x in grid:
    line = ""
    for y in x:
        line += str(y)
    print(line)
