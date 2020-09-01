# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:18:16 2019

@author: DELL
"""
n = 232792560  # smallest number that is divisible to all numbers in the range i

for i in range(1, 21):
    remainder = n % i
    if remainder == 0:
        print("True", i)
