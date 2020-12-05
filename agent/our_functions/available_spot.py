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
            Each integer represent idx in 1D map.
    """
    
    empty = 0
    allie = color
    enemy = -color

    available_spot = []
    # available_spot = set()

    for pos in range(64):
        piece = obs[pos]

        if piece == allie:
            row, col = pos//8, pos%8

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    can_attack = False
                    chk_row, chk_col = (row)+j, (col)+i

                    while (chk_row >= 0 and chk_col >= 0
                            and chk_row < 8 and chk_col < 8):
                        chk_pos = 8*chk_row + chk_col
                        
                        if obs[chk_pos] == enemy:
                            can_attack = True
                        
                        elif obs[chk_pos] == allie:
                            break
                        
                        elif obs[chk_pos] == empty:
                            if can_attack and chk_pos not in available_spot:
                                available_spot.append(chk_pos)
                            # if can_attack:
                            #     available_spot.add(chk_pos)
                            break
                        chk_row += j
                        chk_col += i
    
    return available_spot

if __name__ == "__main__":
    test_board = [ 0,  0,  0,  0,  0,  0,  0,  0,
                   0,  0,  0,  0,  0,  0,  0,  0,
                   0, -1, -1, -1, -1, -1,  0,  0,
                   0, -1,  1,  1,  1, -1,  0,  0,
                   0, -1,  1, -1,  1,  1,  0,  0,
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
            if 8*i+j in test:
                print("x", end=" ")
            else:
                print("0", end=" ")
        print("") 
    # print(test)