# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:22:21 2022

@author: nolan

1. append() - add item in to the list
2. list.len() - cannot be looped directly without range()
3. sep - combine the elements with spaces in a print
4. x = "X-CAMP" - set up input as static string for easiness dev
5. input is immutable 

"""

x = input()
t1 = []
t2 = []

for i in range(len(x)):
    if i%2==0:
        t1.append(x[i])
    else:
        t2.append(x[i])

print(*(t1+t2), sep = "")