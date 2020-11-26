def getAvailableSpot(obs, color):
    """
    Parameters
    -----------
    obs: dict 
        board status

        key: int 0 ~ 63
        value: [-1, 0 ,1]
                -1 : black
                0 : empty
                1 : white
    
    Returns
    -----------
    list of tuples
    """
    
    board = [obs[8*row:8*row+8] for row in range(8)]
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

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == allie:
                is_available = False
                
                # check left
                can_attack = False
                for chk_col in range(col-1, -1, -1):
                    if board[row][chk_col] == enemy:
                        can_attack = True
                    elif board[row][chk_col] == allie:
                        break
                    else:
                        if can_attack:
                            is_available = True
                        break
                if is_available:
                    available_spot.append((col, row))
                    continue
                
                # check right
                can_attack = False
                for chk_col in range(col+1, 8):
                    if board[row][chk_col] == enemy:
                        can_attack = True
                    elif board[row][chk_col] == allie:
                        break
                    else:
                        if can_attack:
                            is_available = True
                        break
                if is_available:
                    available_spot.append((col, row))
                    continue
                
                # check up
                can_attack = False
                for chk_row in range(row-1, -1, -1):
                    if board[chk_row][col] == enemy:
                        can_attack = True
                    elif board[chk_row][col] == allie:
                        break
                    else:
                        if can_attack:
                            is_available = True
                        break
                if is_available:
                    available_spot.append((col, row))
                    continue
                
                # check down
                can_attack = False
                for chk_row in range(row+1, 8):
                    if board[chk_row][col] == enemy:
                        can_attack = True
                    elif board[chk_row][col] == allie:
                        break
                    else:
                        if can_attack:
                            is_available = True
                        break
                if is_available:
                    available_spot.append((col, row))
                    continue
                
                # check diagnal
                
            else:
                continue

    
    
    return available_spot