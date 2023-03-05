# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:24:51 2022

@author: nolan
"""

n, m, o = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []

def merge_two_list(a, b):
    m = len(a)
    n = len(b)
    e = []
    for i in range(n+m):
        if len(a) == 0:
            e.append(b.pop(0))
        elif len(b) == 0:
            e.append(a.pop(0))
        else:
            if a[0] > b[0]:
                e.append(b.pop(0))
            else:
                e.append(a.pop(0))
    return e

e = merge_two_list(b, c)
f = merge_two_list(e, a)
print(*f)
