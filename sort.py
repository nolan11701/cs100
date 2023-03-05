# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:47:35 2022

@author: nolan
"""

def bubble_sort(m):
    n = len(m)
    for i in range(n-1):
        for j in range(n-1-i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    return m

def selection_sort(m):
    n = len(m)
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            if m[j] < m[pos]:
                pos = j
        m[i], m[pos] = m[pos], m[i]
    
    return m

def insersion_sort(m):
    n = len(m)
    for i in range(1, n):
        c = m[i]
        for j in range(i, -1, -1):
            if c < m[j-1] and j>0:
                m[j] = m[j-1]
            else:
                m[j] = c
                break
 
    return m


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n%i == 0:
            return False
        else:
            continue
    return True
           
             