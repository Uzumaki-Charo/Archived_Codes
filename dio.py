# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:33:23 2020

@author: DELL
"""
import math as m

def sol_equa(n):
    result=[]       #define solutions
    nn=finding(n)   #calling finding function
    for i in range(0,len(nn)):
        x=f(nn[i][0],nn[i][1])
        y=g(nn[i][0],nn[i][1])
        if testing(x,y,n):
            result.append([x, y])
    return result
            
def f(n,m):         #find x
    return (n+m)//2
def g(n,m):         #find y
    return (m-n)//4
def testing(x,y,n):     #check if the two sides equal
    if (x-2*y)*(x+2*y)==n:
        return True
    else: return False
def finding(n):     #find the multiple of n(???)
    nn=[]
    j=0
    for i in range(1,int(m.sqrt(n)+1)):
        if n%i==0:
            j=n//i
            nn.append([i,j])
    return nn
    
    
print(sol_equa(12))