def print_sudoku(sudoku: list):
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("")
        row = ""
        for j in range(9):
            if j > 0 and j % 3 == 0:
                row += " "
            if sudoku[i][j] == 0:
                row += "_ "
            else:
                row += str(sudoku[i][j]) + " "
        print(row)

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_grid = []
    for row in sudoku:
        new_grid.append(row[:])
    new_grid[row_no][column_no] = number
    return new_grid

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)