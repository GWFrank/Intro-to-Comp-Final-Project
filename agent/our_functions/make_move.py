def makeMove(obs, move, color):
    """
    Parameters
    -----------
    obs:    1D-list
            1D array of the board

    move:   tuple
            where to place the piece (x, y)
            
            col x : 0 ~ 7   left -> right
            row y : 0 ~ 7   top  -> bottom
    
    color:  int
            who's making a move

            1  -> white
            -1 -> black

    Returns
    -----------
    list
            1D array of the board
    """
    # board = [obs[8*row:8*row+8] for row in range(8)]
    obs = obs.copy()

    empty = 0
    allie = color
    enemy = -color
    

    col, row = move

    for horz in [-1, 0, 1]:
        for vert in [-1, 0, 1]:
            # if horz != 0 or vert != 0:
            #     something
            # else:
            #     pass
            chk_row, chk_col = row+vert, col+horz
            flipping_pos = []

            while (chk_row >= 0 and chk_col >= 0
                    and chk_row < 8 and chk_col < 8):
                
                if obs[8*chk_row + chk_col] == enemy:
                    flipping_pos.append(8*chk_row + chk_col)
                
                elif obs[8*chk_row + chk_col] == allie:
                    if flipping_pos != []:
                        for p in flipping_pos:
                            obs[p] = allie
                        obs[8*row + col] = allie
                    break
                
                elif obs[8*chk_row + chk_col] == empty:
                    break

                chk_row += vert
                chk_col += horz
    
    return obs

if __name__ == "__main__":
    test_board = [ 0,  0,  0,  0,  0,  0,  0,  0,
                   0,  0,  0, -1,  0,  0,  0,  0,
                   0,  0,  1,  0,  0,  0,  0,  0,
                   0,  0,  1,  1,  1, -1,  0,  0,
                   0,  1,  1,  1,  1,  0,  0,  0,
                   0,  1,  1,  1,  1,  0,  0,  0,
                   0, -1,  0,  0, -1,  0,  0,  0,
                   0,  0,  0,  0,  0,  0,  0,  0 ]

    test = makeMove(test_board, (1, 3), -1)
    for i in range(8):
        for j in range(8):
            print(f"{test[8*i + j]:2}", end=" ")
        print("") 