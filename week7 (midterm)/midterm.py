# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:54:10 2022

@author: nolan
"""

# 1.

# x = int(input())
# b = list(map(int, input().split()))

# b.sort()
# z = int((x-1)/2)
# print(b[z])

# 2.

# n = int(input())
# d = []
# m = []
# for look in range(n):
#     x = int(input())
#     d.append(x)
# d.sort()
# l = 0
# r = len(d)-1
# for i in range(0, n):
#     if i%2 == 0:
#         m.append(d[r])
#         r -= 1
#     else:
#         m.append(d[l])
#         l += 1
# print(*m)

# 3.

# n, m = map(int, input().split())
# d = []
# x = [[0 for i in range(m)] for i in range(n)]
# for i in range(n):
#     s = list(map(int, input().split()))
#     d.append(s)
# d.sort()
# for b in d:
#     print(*b)        

# 4.

# d = []

# for i in range(5):
#     x = list(map(int, input().split()))
#     d.append(x)
# for j in range(len(d)):
#     for b in range(5):
#         if d[j][b] == 1:
#             print((max(3,j+1)-min(3,j+1)) + (max(3,b+1)-min(3,b+1)))
#             break

# 5.

x = int(input())
b = list(map(int, input().split()))
y = []
count = 0
z = 0
for i in range(1, len(b)):
    if b[i] < b[i-1]:
        count+=1
if count >= 2:
    z = -1
elif count ==0:
    z = 0
else:
    for j in range(1, len(b)):
        if b[j] < b[j-1]:
            b.insert(0, b.pop())
            z += 1
print(z)                
                