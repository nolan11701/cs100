# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:10:39 2022

@author: nolan

1. model the input to save testing time
2. list.append to add elements
3. resverse() doesnot need a variable
4. toggle 1,0 - use 1-x
5. print matrix inside the for loop, row by row
6. change the value of list by accesing the element then = sign
7. j loop should be nested 

"""

n = int(input())
nlist = []

for i in range(n):
    nlist.append(list(map(int, input().split())))

for i in range(n):
    nlist[i].reverse()
    for j in range(n):
        nlist[i][j] = 1 - nlist[i][j]
x    print(*nlist[i])