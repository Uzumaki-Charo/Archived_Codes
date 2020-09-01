# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:33:50 2019

@author: DELL
"""

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
    j=3;
    h=True;
    while h:
        if checkprime(n):
            j=n;
            i=i+1;
        if i==10001:
            print("j=",j);
            h=False;
        n=n+2;   
            
findingprime(5);