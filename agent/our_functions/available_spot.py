def getAvailableSpot(obs, color):
    """
    Parameters
    -----------
    obs:    1D-list
            1D array of the board
    # board:  2D-list
    #        2D array of the board
    
    color:  string
            getting who's available spot

            "black" or "white"
    
    Returns
    -----------
    list(tuple)
            Each tuple represent cordinate of a available spot (x, y).
            x : int 0 ~ 7
            y : int 0 ~ 7
    """
    
    # board = [obs[8*row:8*row+8] for row in range(8)]
    # print(board)
    empty = 0
    if color == "black":
        allie = -1
        enemy = 1
    elif color == "white":
        allie = 1
        enemy = -1
    else:
        raise ValueError
    

    available_spot = []

    def chk_atk(horz, vert, row, col):
        nonlocal available_spot, allie, enemy, empty
        
        can_attack = False
        chk_row, chk_col = row+vert, col+horz
        while (chk_row >= 0 and chk_col >= 0
                and chk_row < 8 and chk_col < 8):
            if obs[8*chk_row + chk_col] == enemy:
                can_attack = True
            elif obs[8*chk_row + chk_col] == allie:
                break
            elif obs[8*chk_row + chk_col] == empty:
                if can_attack:
                    available_spot.append((chk_col, chk_row))
                break
            else:
                raise ValueError

            chk_row += vert
            chk_col += horz

    for row in range(8):
        for col in range(8):
            piece = obs[8*row + col]
            if piece == allie:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i**2+j**2 > 0:
                            chk_atk(i, j, row, col)    
            else:
                continue

    return available_spot

if __name__ == "__main__":
    test_board = [ 0,  0,  0,  0,  0,  0,  0,  0,
                   0,  0,  0,  0,  0,  0,  0,  0,
                   0, -1, -1, -1, -1, -1,  0,  0,
                   0, -1,  1,  1,  1, -1,  0,  0,
                   0, -1,  1, -1,  1, -1,  0,  0,
                   0, -1,  1,  1,  1, -1,  0,  0,
                   0, -1, -1, -1, -1, -1,  0,  0,
                   0,  0,  0,  0,  0,  0,  0,  0 ]
    
    # test_board = [ 0,  0,  0,  0,  0,  0,  0,  0,
    #                0,  0,  0,  0,  0,  0,  0,  0,
    #                0,  0,  0,  0,  0,  0,  0,  0,
    #                0,  0,  0,  0,  0,  0,  0,  0,
    #                0,  0,  0,  0,  0,  0,  1,  1,
    #                0,  0,  0,  0,  0,  0,  1, -1,
    #                0,  0,  1,  1,  1,  1,  1,  0,
    #                0,  0,  1,  0,  1, -1, -1,  1 ]

    test = getAvailableSpot(test_board, "white")
    for i in range(8):
        for j in range(8):
            if (j, i) in test:
                print("x", end=" ")
            else:
                print("0", end=" ")
        print("") 