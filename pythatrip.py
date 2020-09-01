# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:09:49 2019

@author: DELL
"""
import math
h=True;
while h==True:
    for i in range(1,1000):
        a=i;
        for j in range(1,1000):
            b=j;
            if a<b:
                c2=(a*a)+(b*b);
                if math.sqrt(c2)==int(math.sqrt(c2)):
                    c=math.sqrt(c2);
                    if (a+b+c==1000):
                        print(a,b,c);
                        print(a*b*c);
                        h=False;
                