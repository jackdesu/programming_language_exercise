def win_by_row(game, who):
    for x in range(0, 3):
        win = True
        for y in range(0, 3):
            if game[x][y] != who:
                win = False
                break
        if win:
            return win
    return win


def win_by_column(game, who):
    for x in range(0, 3):
        win = True
        for y in range(0, 3):
            if game[y][x] != who:
                win = False
                break
        if win:
            return True
    return win


def win_by_cross(game, who):
    if game[0][0] == who and game[1][1] == who and game[2][2] == who:
        return True
    elif game[0][2] == who and game[1][1] == who and game[2][0] == who:
        return True
    else:
        return False


def find_winner(game, who):
    return win_by_row(game, who) or win_by_column(game, who) or win_by_cross(game, who)

game = [[2, 0, 0], [2, 1, 0], [2, 1, 1]]

if find_winner(game, 1):
    print "winner is 1"
elif find_winner(game, 2):
    print "winner is 2"
else:
    print "drew"
