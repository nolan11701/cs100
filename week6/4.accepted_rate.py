# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:41:58 2022

@author: nolan
"""


x = list(map(str, input()))
y = x[:-1]

A = 0
W = 0
C = 0

for i in range(len(y)):
    if y[i] == 'A':
        A += 1
    elif y[i] == 'W':
        W += 1
    elif y[i] == 'C':
        C += 1

formater = '{:.2f}'

b = [A/len(y),W/len(y),C/len(y)]
e = [formater.format(i) for i in b]
print(*e, sep = '\n')