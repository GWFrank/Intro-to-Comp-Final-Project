def makeMove(obs, move, color):
    """
    Parameters
    -----------
    obs:    1D-list
            1D array of the board

    move:   int
            where to place the piece
            index for obs
    
    color:  int
            who's making a move

            1  -> white
            -1 -> black

    Returns
    -----------
    list
            1D array of the board
    """

    obs = obs.copy()

    empty = 0
    allie = color
    enemy = -color
    

    row, col = move//8, move%8

    for horz in [-1, 0, 1]:
        for vert in [-1, 0, 1]:
            chk_row, chk_col = row+vert, col+horz
            flipping_pos = []

            while (chk_row >= 0 and chk_col >= 0
                    and chk_row < 8 and chk_col < 8):
                chk_pos = 8*chk_row + chk_col

                if obs[chk_pos] == enemy:
                    flipping_pos.append(chk_pos)
                
                elif obs[chk_pos] == allie:
                    if flipping_pos != []:
                        for p in flipping_pos:
                            obs[p] = allie
                        obs[move] = allie
                    break
                
                elif obs[chk_pos] == empty:
                    break

                chk_row += vert
                chk_col += horz
    
    return obs

if __name__ == "__main__":
    test_board = [ 0,  0,  0,  0,  0,  0,  0,  0,
                   1,  0,  0, -1,  0,  0,  0,  0,
                  -1,  0,  1,  0,  0,  0,  0,  0,
                   0,  0,  1,  1,  1, -1,  0,  0,
                   0,  1,  1,  1,  1,  0,  0,  0,
                   0,  1,  1,  1,  1,  0,  0,  0,
                   0, -1,  0,  0, -1,  0,  0,  0,
                   0,  0,  0,  0,  0,  0,  0,  0 ]

    # test_board = [ 0,  0,  1, -1, -1, -1, -1, -1, 
    #               -1,  0,  1, -1, -1,  1,  1, -1, 
    #                1, -1,  1, -1,  1, -1,  1, -1, 
    #                1,  1, -1,  1, -1,  1,  1, -1, 
    #                1,  1,  1, -1,  1, -1,  1, -1, 
    #                1,  1, -1, -1,  1,  1,  1, -1, 
    #                1, -1, -1,  1,  1,  1,  1, -1, 
    #                0,  0,  1,  1,  1,  1,  0,  0 ]

    test = makeMove(test_board, (8*0 + 0), 1)
    for i in range(8):
        for j in range(8):
            print(f"{test[8*i + j]:2}", end=" ")
        print("") 