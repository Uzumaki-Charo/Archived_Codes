# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:24:22 2019

@author: DELL
"""

n=2**1000
m=0
while n!=0:
    m=m+n%10
    n=n//10
print(m)