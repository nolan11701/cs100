# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:24:21 2022

@author: nolan
"""

n, k = map(int, input().split())
l = list(map(int, input().split())) 
b = 10
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

xb, mb = 0, 10
for bucket in all_buckets:
    if len(bucket) > xb:
        xb = len(bucket)
    if len(bucket) < mb:
        mb = len(bucket)
if xb-mb >= k:
    print("Yes")
else:
    print("No")    