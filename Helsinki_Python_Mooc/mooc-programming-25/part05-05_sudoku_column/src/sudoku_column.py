# Write your solution here
def column_correct(sudoku: list, column_no: int):
    found_nums = []
    for i in sudoku:
        if i[column_no] in found_nums:
            return False
        elif i[column_no] > 0:
            found_nums.append(i[column_no])
    return True
