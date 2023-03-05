# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:07:18 2022

@author: nolan
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

a = input()
i = int(input())
m = []

for j in range(len(a)):
    n = alphabet.index(a[j])+i
    m.append(alphabet[n%26])

print(''.join(m))