# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:37:22 2022

@author: nolan
"""

from copy import deepcopy
from time import sleep
from random import randint, shuffle

S = 19
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# Player 1's Part
def Player1MoveOneStep(board, ty):
    # Should return coordination to represent a move
    t = input()
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = t[0]
    b = t[1:]
    x = s.index(a)
    y = int(b)-1
    return y,x 


# Player 2's Part
def Player2MoveOneStep(board, ty):
    # Should return coordination to represent a move
    t = input()
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = t[0]
    b = t[1:]
    x = s.index(a)
    y = int(b)-1
    return y,x 



# Ruler's Part
def PrintBoard(board):
    """Print the current board.
    _: empty
    o: player 1
    x: player 2
    O/X: the positions which let one win (only appear when the game is finished)
    """
    print()
    print("   ", end="")
    s = len(board[0])
    a = 65
    for i in range(s):
        print(chr(a+i), end = " ")
    print()
    for i in range(len(board)):
        if i<9:
            print(" ",end="")
        print(i+1, end = " ")
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
    return
    


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
        CheckBoard(board)
        sleep(0.2)

        # Player2's turn
        x, y = Player2MoveOneStep(deepcopy(board), type2)
        if 0 <= x and x < S and 0 <= y and y < S and board[x][y] == 0:
            board[x][y] = 2
        else:
            print("Player2 breaks the rule")
            exit(0)
        PrintBoard(board)
        CheckBoard(board)
        sleep(0.2)