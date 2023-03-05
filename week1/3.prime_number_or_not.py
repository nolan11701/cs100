# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 11:40:41 2022

1. check for special cases, e.g. 1, 2, 0
2. for boolean variable, if var:. no need to use "== True"
3. x/2+1 is float type - use //
4. To improve efficiency, don't include large numbers, int(x**0.5)
"""

x = int(input())
prime = True

for i in range(2, int(x**0.5+1)):
    if x%i==0:
        prime = False
if x == 1:
    prime = False

if prime:
    print("Yes")
else:
    print("No")