# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:03:55 2022

@author: nolan
"""
def merge(a, b):
    merged = []
    a_pos, b_pos = 0, 0 # since lists are sorted, start at each lists smallest value, at index 0
    while a_pos < len(a) and b_pos < len(b): # compare smallest in a to smallest in b, so long as neither are finished
        if a[a_pos] < b[b_pos]:
            merged.append(a[a_pos]) # place the smaller item between a and b in the list
            a_pos += 1 # move to the next index if the value was used
        else:
            merged.append(b[b_pos])
            b_pos += 1
    while a_pos < len(a): # if list b finished, but list a has more items left, empty list a into the merged list
        merged.append(a[a_pos])
        a_pos += 1
    while b_pos < len(b): # same thing if it is the case for b
        merged.append(b[b_pos])
        b_pos += 1
    return merged # send back the merged list

def merge_sort(lst):
    n = len(lst)
    segment_size = 1 # always start with the smallest possible sorted lists, lists of size 1
    while segment_size < n:
        start_pos = 0
        merged_itms = [] # here is where we will put our merged items. we will replace our list with our merged list at the end of each loop
        while start_pos < n:
            a_pos = start_pos # initialize our start and end points for our two lists
            a_end = min(a_pos + segment_size, n)
            b_pos = a_end
            b_end = min(b_pos + segment_size, n)
            c = merge(lst[a_pos:a_end], lst[b_pos:b_end]) # merge the two lists to get a new list of size len(a) + len(b)
            merged_itms.extend(c) # add our merged list to what we have so far
            start_pos += 2 * segment_size # move our starting point to the next interval
        segment_size *= 2 # once we loop through and merge the entire list, double our segment size for next round
        lst = merged_itms # change the list we have to the merged one we just created
    return lst

n = int(input())
m = list(map(int, input().split()))
l = merge_sort(m)
print(*l)