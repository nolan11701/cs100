# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:36:42 2022

@author: nolan
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a+b
c.sort()
print(*c)