# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:45:18 2022

@author: nolan

1. split() can break a str to list by space
2. pop(int index) will remove the element from the list, index is int  
3. if i<x is better than i>=x, because it is more efficient for the computer
4. break - when the loop is not necessary
5. map(func, list()) - iterate the list and run the func on each element, and return the result as a new list 

"""
x = int(input())
y = input()
z = list(y.split())

for i in range(len(z)):
    if i<x:
        print(z[i], end=" ")
    else:
        break