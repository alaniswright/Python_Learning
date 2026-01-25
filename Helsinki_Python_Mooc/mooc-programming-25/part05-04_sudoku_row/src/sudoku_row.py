# Write your solution here
def row_correct(sudoku: list, row_no: int):
    found_nums = []
    for i in sudoku[row_no]:
        if i in found_nums:
            return False
        elif i > 0:
            found_nums.append(i)
    return True

