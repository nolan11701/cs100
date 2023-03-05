# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:20:57 2022

@author: nolan
# =============================================================================
# """
# b = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,1,0,2,0,0,0,0,0,0,0,0,0,0,0],
# [0,1,0,2,0,0,0,0,0,0,0,0,0,0,0],
# [0,1,0,2,0,0,0,0,0,0,0,0,0,0,0],
# [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# =============================================================================

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


def CheckBoard(board):
    """Check if the game is finished.
    If so, print the final board and exit the program.
    """
    S = len(board)
    dx = [1, 1, 1, 0, -1, -1, -1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    count_zero = 0
    for x in range(S):
        for y in range(S):
            if board[x][y] == 0:
                count_zero += 1
                continue 
            
            for d in range(8):
                x_dir = x + (dx[d] * 4)
                y_dir = y + (dy[d] * 4)
                # print("\n===")
                # print(x_dir, y_dir)
                if x_dir<0 or x_dir>14 or y_dir<0 or y_dir>14:
                      continue
                valid = True
                for i in range(5):
                    # if the cell being visited does not match (x, y):
                    if board[x][y] != board[x + (dx[d] * i)][y + (dy[d] * i)]:
                        #print(x + (dx[d] * i), y + (dy[d] * i), end = ' |')
                        #print(board[x + (dx[d] * i)][y + (dy[d] * i)], end = ' ')
                        valid = False
                if valid == True:
                    t = "Player {} wins\n".format(board[x][y])
                    for i in range(5):
                        # add 2 to each of these cells to mark the winning pieces
                        board[x + (dx[d] * i)][y + (dy[d] * i)] += 2
                    #PrintBoard(board)
                    #exit(0)
                    return t

            
            # Iterate over matrix and if we don't see any 0's:
    if count_zero == 0:
        return "Tie"
    #     exit(0)
    return "Continue game"

n = 15
b = []
for i in range(n):
    b.append(list(map(int, input().split()))) 
# PrintBoard(b)
print(CheckBoard(b))