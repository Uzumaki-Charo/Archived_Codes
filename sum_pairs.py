# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:19:31 2020

@author: DELL
"""

def sum_pairs(ints, s):
    jj=len(ints)-1
    ii=0
    k=0
    for i in range(len(ints)):
        for j in range(i+1,len(ints)):
            if ints[i]+ints[j]==s:
                if j<=jj:
                    jj=j
                    ii=i
                k=1
    return [ ints[ii], ints[jj] ] if k==1 else None
            
                
l2= [1, -2, 3, 0, -6, 1] 
l5= [10, 5, 2, 3, 7, 5]            
#print(sum_pairs(l2, -6))
print(sum_pairs(l5, 10))         

def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
        
    
    
