# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:33:50 2019

@author: DELL
"""
#find the sum of prime numbers less than 2M

import math


def checkprime(n):

    for i in range(3,int(math.sqrt(n)) + 1, 2): 
        if n % i == 0:
            #print("not",n);
            return False;
    #print("prime",n);
    return True;
def findingprime(n):
    i=2;
    j=2;
    h=True;
    
    while h:
        if n>2000000:
            print("sum=",j);
            h=False;
        if checkprime(n):
            j=j+n;
            i=i+1;
        n=n+2;   
            
findingprime(3);