def win_by_lin(game, who, row):
    for x in range(0, 3):
        win = True
        for y in range(0, 3):
            if row:
                if game[x][y] != who:
                    win = False
                    break
            else:
                if game[y][x] != who:
                    win = False
                    break
        if win:
            return win
    return win


def win_by_row(game, who):
    return win_by_lin(game, who, True)


def win_by_column(game, who):
    return win_by_lin(game, who, False)


def win_by_cross(game, who):
    if game[0][0] == who and game[1][1] == who and game[2][2] == who:
        return True
    elif game[0][2] == who and game[1][1] == who and game[2][0] == who:
        return True
    else:
        return False


def find_winner(game_to_judge, who):
    return win_by_row(game_to_judge, who) or \
           win_by_column(game_to_judge, who) or \
           win_by_cross(game_to_judge, who)


def game_over_if_someone_won(game_to_judge):
    if find_winner(game_to_judge, 1):
        print "1 is winner"
        return True
    elif find_winner(game_to_judge, 2):
        print "2 is winner"
        return True
    else:
        return False


def get_next_player(current_player):
    if 1 == current_player:
        return 2
    else:
        return 1


game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
moves = 0
player = 1

while True:
    drop = raw_input("player " + str(player) + " please enter your move (x, y): ")
    move = drop.split(",")

    current_x = int(move[0])-1
    current_y = int(move[1])-1
    if game[current_x][current_y] != 0:
        print "used, please try other move"
    else:
        game[current_x][current_y] = player
        moves += 1
        player = get_next_player(player)

    if game_over_if_someone_won(game):
        break

    if moves >= 9:
        print "no more move, game drew"
        break

    print game
