# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:56:11 2022

@author: nolan
"""

# # input n i j
# n = 4
# i = 2
# j = 3
n, i, j = map(int, input().split())
# make an empty matrix with n
m = [[0 for i in range(n)] for i in range(n)]
# add spiral elements to the matrix
x = 0
y = -1
# top left bottom right are boundaries 
top, left = 0, 0
bottom, right = n-1, n-1
# t is the counter 
t = n**2
# d is direction 0 - right 1 - down 2 - left 3 - up
d = 0
while t != 0:
    t -= 1
    
    if d == 0:
        y+=1
        if (y==right):
            d = 1
            top+=1
    elif d == 1:
        x+=1
        if (x==bottom):
            d = 2
            right-=1
    elif d == 2:
        y-=1
        if (y==left):
            d+=1
            bottom-=1
    elif d == 3:
        x-=1
        if (x==top):
            d=0
            left+=1
    m[x][y]=n**2-t

print(m[i-1][j-1])