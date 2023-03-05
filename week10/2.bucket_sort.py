# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:24:21 2022

@author: nolan
"""

import math
n = input()
l = list(map(int, input().split()))

b = math.floor(math.sqrt(max(l))) + 1
all_buckets = []
for i in range(b):
    all_buckets.append([])

def insertion(bucket):
    itm_to_insert = all_buckets[bucket][-1]
    curr_pos = len(all_buckets[bucket]) - 1
    while curr_pos > 0 and itm_to_insert < all_buckets[bucket][curr_pos-1]:
        all_buckets[bucket][curr_pos] = all_buckets[bucket][curr_pos-1]
        curr_pos-=1
    all_buckets[bucket][curr_pos] = itm_to_insert

for itm in l:
    position = itm//b
    all_buckets[position].append(itm)
    if len(all_buckets[position]) > 1:
        insertion(position)

sorted_lst = []
for bucket in all_buckets:
    for itm in bucket:
        sorted_lst.append(itm)
    
print(*sorted_lst)