# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:28:28 2019

@author: DELL
"""

i=0
#n=16
#h=True
#while h:
#    if n<1000000:
#        if (n-1)/3==int((n-1)/3):
#            n=(n-1)/3
#            i=i+1
#        else:
#            n=n*2
#            i=i+1
#    else:
#        h=False
#
#print(n,i,1572864/2)
maxp=-1
#n=837799
array=[0]*1000
for n in range(1000000,77032,-1):
    m=n
    while n!=1:
        if n%2==0:
            n=n/2
            i=i+1
        else:
            n=(3*n)+1
            i=i+1
    if i>maxp:
        maxp=i
        array[maxp]=m
    i=0;
    
print(array[maxp],maxp)
#n=0
#for i in range(399,23,-1):
#    n=n+3
#    
#print(n)
