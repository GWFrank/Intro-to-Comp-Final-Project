def makeMove(obs, move, color):
    """
    Parameters
    -----------
    obs:    1D-list
            1D array of the board
    
    # board:  2D-list
    #         2D array of the board

    move:   tuple
            where to place the piece (x, y)
            
            col x : 0 ~ 7   left -> right
            row y : 0 ~ 7   top  -> bottom
    
    color:  string
            getting who's available spot

            "black" or "white"

    Returns
    -----------
    list(list)
            2D array of the board
    """
    # board = [obs[8*row:8*row+8] for row in range(8)]
    obs = obs.copy()

    empty = 0
    if color == "black":
        allie = -1
        enemy = 1
    elif color == "white":
        allie = 1
        enemy = -1
    else:
        raise ValueError

    col, row = move

    # def _flip(pos):
    #     nonlocal obs
    #     for p in pos:
    #         obs[8*p[0] + p[1]] *= -1

    for horz in [-1, 0, 1]:
        for vert in [-1, 0, 1]:
            if horz**2 + vert**2 > 0:
                chk_row, chk_col = row+vert, col+horz
                flipping_pos = []

                while (chk_row >= 0 and chk_col >= 0
                        and chk_row < 8 and chk_col < 8):
                    
                    if obs[8*chk_row + chk_col] == enemy:
                        flipping_pos.append((chk_row, chk_col))
                    
                    elif obs[8*chk_row + chk_col] == allie:
                        if flipping_pos != []:
                            # _flip(flipping_pos)
                            for p in flipping_pos:
                                obs[8*p[0] + p[1]] *= -1
                            obs[8*row + col] = allie
                        break
                    
                    elif obs[8*chk_row + chk_col] == empty:
                        break
                    
                    else:
                        raise ValueError

                    chk_row += vert
                    chk_col += horz
            else:
                pass
    
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

    test = makeMove(test_board, (1, 3), "black")
    for i in range(8):
        for j in range(8):
            print(f"{test[8*i + j]:2}", end=" ")
        print("") 