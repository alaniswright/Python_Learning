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
