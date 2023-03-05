# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:08:26 2022

@author: nolan

learnings 
1. sort first then remove dup 
2. left pointer and right pointer 
3. bubble sort is not effecient enough for this question 
4. bit map - can use to filter list
"""

# n = 10
# m = [10, 9, 9,9,9]
# 
#def find_bit_map(m, e):

    
# z = [1 for i in range(len(m))]
# count  = 0
# for i in range(len(m)):
#     for j in range(i+1, len(m)):
#         count += 1
#         if m[j]==m[i]:
#             z[j] = 0
# p = []
# for i in range(len(m)):
#     if z[i] == 1:
#         p.append(m[i])
        
    
n = int(input())
m = list(map(int, input().split()))

# bubble sort doesn't work due to memory limitation
m.sort()

l = 1

for r in range(1, n):
    if m[r] != m[r-1]:
        m[l] = m[r]
        l+=1

print(*m[0:l])