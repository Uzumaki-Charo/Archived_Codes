# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:20:11 2019

@author: DELL
"""
#find the difference between the sum of square and square of sum

sum1=0;
sum2=0;
for i in range(1,101):
    sum1=sum1+i*i;
    sum2=sum2+i;
print("",sum2*sum2-sum1)
