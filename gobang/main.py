# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:37:22 2022

@author: nolan
"""

from copy import deepcopy
from time import sleep

S = 15
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def PlayerMove(board, ty):
    # Should return coordination to represent a move
    t = input()
    s = "123456789abcdef"
    a = t[0]
    b = t[1:]
    x = s.index(a)
    y = s.index(b)

    return y, x

# Player 1's Part
def Player1MoveOneStep(board, ty):
    return PlayerMove(board, ty)

# Player 2's Part
def Player2MoveOneStep(board, ty):
    return PlayerMove(board, ty)


# Ruler's Part
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
                    PrintBoard(board)
                    #exit(0)
                    return t

            # Iterate over matrix and if we don't see any 0's:
    if count_zero == 0:
        return "Tie"
    #     exit(0)
    return "Continue game"
    


if __name__ == "__main__":
    # Here the ruler organize the game and ask players to act by turns.
    type1 = int(input("Player 1:\n1) Human \n2) AI \nType 1 or 2: "))
    type2 = int(input("Player 2:\n1) Human \n2) AI \nType 1 or 2: "))
    assert type1 in {1, 2} and type2 in {1, 2}
    turn = 0
    board = [[0] * S for i in range(S)]
    PrintBoard(board)
    while (True):
        turn += 1
        print("=========== turn {} ===========".format(turn))
        # Player1's turn
        x, y = Player1MoveOneStep(deepcopy(board), type1)
        if 0 <= x and x < S and 0 <= y and y < S and board[x][y] == 0:
            board[x][y] = 1
        else:
            print("Player1 breaks the rule")
            exit(0)
        PrintBoard(board)
        t= CheckBoard(board)
        print(t)
        if t.startswith("Player") or t.startswith("Tie"):
            exit(0)
        sleep(0.2)

        # Player2's turn
        x, y = Player2MoveOneStep(deepcopy(board), type2)
        if 0 <= x and x < S and 0 <= y and y < S and board[x][y] == 0:
            board[x][y] = 2
        else:
            print("Player2 breaks the rule")
            exit(0)
        PrintBoard(board)
        t= CheckBoard(board)
        print(t)
        if t.startswith("Player") or t.startswith("Tie"):
            exit(0)
        sleep(0.2)