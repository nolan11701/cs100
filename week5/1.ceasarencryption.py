# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:28:35 2022

@author: nolan
"""
a = 'abcdefghijklmnopqrstuvwxyz'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s, e = input().split()
d = []
for i in s:
    # check if i is in a
    if i in a:
        b = a.index(i)
        n = b+int(e) 
        
        d.append(a[n%26])
       
    elif i in A:
        b = A.index(i)
        n = b+int(e) 
        
        d.append(A[n%26])
       
       
print(*d, sep = "")            
        
    # else return index+e
    # find the char of (index +e  or index+e-26)
    
    # if not in a but in A
    
