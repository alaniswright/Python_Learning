# Write your solution here
def who_won(game_board: list):
    player_1_score = 0
    player_2_score = 0
    for row in game_board:
        for square in row:
            if square == 1:
                player_1_score += 1
            elif square == 2:
                player_2_score += 1
    if player_1_score > player_2_score:
        return 1
    elif player_2_score > player_1_score:
        return 2
    else:
        return 0