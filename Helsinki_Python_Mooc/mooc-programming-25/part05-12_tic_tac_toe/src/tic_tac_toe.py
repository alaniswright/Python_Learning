# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    try:
        if x < 0:
            return False
        if y < 0:
            return False
        print(game_board[y][x])
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
    game_board_2 = [['X', 'O', ''], ['O', '', ''], ['X', '', 'O']]
    print(play_turn(game_board_2, -1, 1, "X"))
    print(game_board_2)