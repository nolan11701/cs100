# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:16:27 2022

@author: nolan
"""

# n = int(input())
# p = []
# for i in range(n):
#     p.append(int(input()))
 
# for m in p:
#     count = 0
#     l = [i for i in range(1, m+1, 2)]
#     for i in range(2, len(l)):
#         #find all multiples of l
#         for j in range(i, len(l)):
#             if l[j] == 0:
#                 continue
#             if l[j] % i == 0:
#                 l[j] = 0
#                 count += 1

#     print(m-count-m//2)


n = int(input())
p = []
for i in range(n):
     p.append(int(input()))
 
n = max(p) + 1

a = [True] * n
b = [0] * n
count = 0

for i in range(2, n):
    if a[i]:
        count += 1    
        for j in range(i*i, n, i):
            a[j] = False
        
    b[i] = count
    
for i in p:
    print(b[i])
    
    