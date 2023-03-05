# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:45:02 2022

@author: nolan
"""

# n = 3
# m = [[1,2,3], [5,1,4], [2,6,5]]
#HELLO
#welcomeToTheLand
#NowLetsSTART
#CODING
#YAY 


n = int(input())
m = []
for f in range(n):
    m.append(list(map(int, input().split())))

for i in range(n):
    k = 0 #row index of min [i,k]
    for j in range(n):
        # find index of min - k
        if m[i][j] < m[i][k]:
            k = j
      #  print(m[i][j])

    h = 0 #col index of max [h, i]
    for j in range(n):
        # find index of max - h
        if m[j][i] > m[h][i]:
            h = j
           # print(m[j][i])

    #print(m[i][k], m[h][i])
    
    # swap 
    # temp = m[i][k] 
    # m[i][k] = m[h][i]
    # m[h][i] = temp
    m[i][k], m[h][i] = m[h][i], m[i][k]
    
    #sort m[i]
    m[i].sort()
    
for i in range(n):
    print(*m[i])