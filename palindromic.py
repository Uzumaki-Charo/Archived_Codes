# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:57:43 2019

@author: DELL
"""

import math
array=[0]*6;
max=-1;
for i in range(1000,1,-1):
    for j in range(1000,1,-1):    
        a=(i)*(j);
        temp=a;
        rev=0;
        while(a>0):
            dig=a%10#get the last digit
            rev=rev*10+dig#building the reversed digits
            a=a//10#removed the last digit
        if(temp==rev):
            if temp>max:
                max=temp
            print("The number is ",max);
            break;

            
#    if (a%11)==0:
#        break;
#        for k in range(0,6):
#            array[k]=a//(10**(5-k));
#            a=a-array[k]*(10**(5-k)); 
            #print("",array);
#            if array[0]==array[5] and array[1]==array[4] and array[2]==array[3]:
#                print("",array);
#                print("",(i)*(j),i,j); 
#        array=[0]*6;

        

            
