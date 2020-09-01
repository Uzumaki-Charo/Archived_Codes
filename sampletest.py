# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:22:33 2020

@author: DELL
"""
import matplotlib
import matplotlib.pyplot as plt


def f(x):
    return (x+1)**2
def g(x):
    return (x-1)**2

x=[1,2,3,4,5]
g=[f(1),f(2),f(3),f(4),f(5)]
plt.plot(x,g)
plt.show()    
print(f(10))