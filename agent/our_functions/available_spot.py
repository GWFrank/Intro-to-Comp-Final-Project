def getAvailableSpot(obs, color):
    """
    Parameters
    -----------
    obs:    1D-list
            1D array of the board
    
    color:  int
            getting who's available spot

            1  -> white
            -1 -> black
    
    Returns
    -----------
    list(int)
            Each int represent index in obs.
    """
    
    # board = [obs[8*row:8*row+8] for row in range(8)]
    
    empty = 0
    allie = color
    enemy = -color
    
    available_spot = []

    for row in range(8):
        for col in range(8):
            piece = obs[8*row + col]
            if piece == allie:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        can_attack = False
                        chk_row, chk_col = row+j, col+i
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
                            chk_row += j
                            chk_col += i
                        # if i != 0 or j != 0:
                        #   original chk_atk()
                        # else:
                        #     continue

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

    test = getAvailableSpot(test_board, 1)
    for i in range(8):
        for j in range(8):
            if (j, i) in test:
                print("x", end=" ")
            else:
                print("0", end=" ")
        print("") 