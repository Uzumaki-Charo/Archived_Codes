# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:04:45 2019

@author: DELL
"""
a1=1;
a2=2;
a=0
sum=2;
while True:
    a=a1+a2;
    a1=a2;
    a2=a;
    remainer=a%2;
    if a>4000000:
        break;
    if remainer==0:
        sum=sum+a;
        
print("sum=",sum,19//100)