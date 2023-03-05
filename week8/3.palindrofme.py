# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:36:18 2022

@author: nolan
"""

x = int(input())

def palindrome(a):
    num = []
    s = 0
    while a != 0:
        num.append(a%10)
        a = a//10
    for i in range(len(num)):
        s += num[i]*10**(len(num)-i-1)
    return s

for i in range(1, x+1):
    if palindrome(i) == i:
        print(i)