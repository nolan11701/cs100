# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:24:43 2022

@author: nolan
"""

dictionary = {}
x = input().split()

for i in x:
    if i in dictionary.keys():
        dictionary[i]+=1
    else:
        dictionary[i]=1

for k,v in dictionary.items():
    print(k, v)