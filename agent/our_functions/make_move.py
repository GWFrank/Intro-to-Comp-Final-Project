def makeMove(board, move, color):
    """
    Parameters
    -----------
    board:  2D-list
            2D array of the board

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

    def _flip(pos):
        nonlocal board
        for p in pos:
            board[p[0]][p[1]] *= -1

    for horz in [-1, 0, 1]:
        for vert in [-1, 0, 1]:
            if horz**2 + vert**2 > 0:
                chk_row, chk_col = row+vert, col+horz
                flipping_pos = []

                while (chk_row >= 0 and chk_col >= 0
                        and chk_row < 8 and chk_col < 8):
                    if board[chk_row][chk_col] == enemy:
                        flipping_pos.append((chk_row, chk_col))
                    elif board[chk_row][chk_col] == allie:
                        if flipping_pos != []:
                            _flip(flipping_pos)
                            board[row][col] = allie
                        break
                    elif board[chk_row][chk_col] == empty:
                        break
                    else:
                        raise ValueError

                    chk_row += vert
                    chk_col += horz
            else:
                pass
    
    return board

if __name__ == "__main__":
    test_board = [ [0,  0,  0,  0,  0,  0,  0,  0],
                   [0,  0,  0, -1,  0,  0,  0,  0],
                   [0,  0,  1,  0,  0,  0,  0,  0],
                   [0,  0,  1,  1,  1, -1,  0,  0],
                   [0,  1,  1,  1,  1,  0,  0,  0],
                   [0,  1,  1,  1,  1,  0,  0,  0],
                   [0, -1,  0,  0, -1,  0,  0,  0],
                   [0,  0,  0,  0,  0,  0,  0,  0] ]

    test = makeMove(test_board, (1, 3), "black")
    for i in range(8):
        for j in range(8):
            print(f"{test[i][j]:2}", end=" ")
        print("") 