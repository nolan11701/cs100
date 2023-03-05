# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:31:02 2022

@author: nolan
"""

x = input()

def is_palindrome(s:str):
    su = list(s)
    su.reverse()
    sup = ''.join(su)
    return sup == s

def find_substring(s:str, l:int):
    sub_strings = []
    for i in range(len(s)):
        if (i+l > len(s)) :
            break
        sub_strings.append(s[i:i+l])
    return sub_strings


for i in range(len(x), 0, -1):
    s = find_substring(x, i)
    
    for j in s:
        if is_palindrome(j):
            print(i)
            break
    else:
        continue 
    break
