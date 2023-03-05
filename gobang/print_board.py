# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:57:17 2022

@author: nolan
"""

def PrintBoard(board):
    """Print the current board.
    _: empty
    o: player 1
    x: player 2
    O/X: the positions which let one win (only appear when the game is finished)
    """
    border = "123456789abcdef"
    print()
    print("  ", end="")

    for i in border:
        print(i, end = " ")
    print()
    for i in range(len(board)):
        print(border[i], end = " ")
        for j in board[i]:
            if j == 0:
                print("_", end = " ")
            elif j == 1:
                print("o", end = " ")
            elif j == 2:
                print("x", end = " ")
            elif j == 3:
                print("O", end = " ")
            elif j == 4:
                print("X", end = " ")
        print()
    print(" ")
    return

# =============================================================================
# 
# b = [[3,0,3,0,3,3,1,0,4,3,0,3,0,0,1],
# [2,1,2,4,1,2,1,2,3,3,4,1,1,1,1],
# [4,3,4,0,2,1,4,4,3,4,3,2,0,2,0],
# [1,0,2,0,0,0,4,1,3,0,0,3,4,0,4],
# [4,2,4,2,3,1,2,0,2,1,3,1,3,2,2],
# [1,2,3,3,1,2,3,4,1,0,4,3,4,1,3],
# [1,4,1,1,4,1,3,4,0,1,3,3,0,0,2],
# [4,1,0,1,2,4,3,4,3,0,2,3,3,3,2],
# [3,1,4,1,2,2,0,3,4,3,0,3,1,0,4],
# [2,2,3,1,2,4,0,3,3,2,2,4,2,4,4],
# [1,0,1,3,3,4,4,1,1,1,0,0,3,3,3],
# [4,4,0,3,2,0,1,4,1,2,0,0,2,2,0],
# [4,1,0,2,2,2,4,2,4,3,2,2,3,2,0],
# [4,3,2,1,2,0,4,2,1,3,1,2,1,4,0],
# [3,4,4,1,3,3,1,2,1,3,2,3,3,0,3]]
# =============================================================================

n = 15
b = []
for i in range(n):
    b.append(list(map(int, input().split()))) 
PrintBoard(b)