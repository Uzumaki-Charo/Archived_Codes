# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:11:35 2019

@author: DELL
"""

def check(n):
    if n==0:
        return int(0)
    elif n==1 or n==2 or n==6 or n==10:
        return 3
    elif n==3 or n==7 or n==8:
        return int(5)
    elif n==4 or n==5 or n==9:
        return int(4)
    elif n==11 or n==12:
        return int(6)
    elif n==13 or n==14 or n==18 or n==19:
        return int(8)
    elif n==15 or n==16:
        return int(7)
    elif n==17:
        return int(9)
    elif n>=20 and n<50:
        return int(6)+check(n%10)
    elif n>=50 and n<70:
        return int(5)+check(n%10)
    elif n>=70 and n<80:
        return int(7)+check(n%10)
    elif n>=80 and n<100:
        return int(6)+check(n%10)
    else:
        raise ValueError(n)

m=0
for i in range(1,100):
    m=m+check(i)
    print(i,m)



sumall=10*854+11+99*(39+42+45)+20+12+22+22+23
print(m,sumall)