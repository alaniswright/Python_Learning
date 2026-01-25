# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    unique = []
    for r in range(row_no, row_no + 3):
        for c in range(column_no, column_no + 3):
            if sudoku[r][c] in unique:
                return False
            elif sudoku[r][c] > 0:
                unique.append(sudoku[r][c])
    return True

# Write your solution here
def column_correct(sudoku: list, column_no: int):
    found_nums = []
    for i in sudoku:
        if i[column_no] in found_nums:
            return False
        elif i[column_no] > 0:
            found_nums.append(i[column_no])
    return True

# Write your solution here
def row_correct(sudoku: list, row_no: int):
    found_nums = []
    for i in sudoku[row_no]:
        if i in found_nums:
            return False
        elif i > 0:
            found_nums.append(i)
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if row_correct(sudoku, i) == False or column_correct(sudoku, i) == False:
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if block_correct(sudoku, i, j) == False:
                return False
    return True
