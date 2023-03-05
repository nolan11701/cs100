# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:08:43 2022

@author: nolan
"""


s = input()
t = s.replace(' ','')
m = list(t)
m.sort()
print(*m, sep="")