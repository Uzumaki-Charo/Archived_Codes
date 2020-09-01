# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:03:43 2020

@author: DELL
"""

def power_sumDigTerm(n):
    #your code here
    arr=[ i for i in range(2,150)]
    me=[0]
    j=2
    while j<10:
        for i in arr:
            x=digsum(i**j)                        
            if x==i:
                me.append(i**j)
                print(i**j)
        j+=1

    me.sort()
    g=me[n]
    return g # n-th term of the sequence, each term is a power of the sum of its digits

def digsum(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum

res1=power_sumDigTerm(10)
#res2=power_sumDigTerm(4)

print("30th",res1)

def power_sumDigTerm(n):
    return sorted([i**j for j in range(2,50) for i in range(2,100) if i == sum([int(i) for i in str(i**j) ])])[n-1]