# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:32:25 2020

@author: DELL
"""

def mystery(n):
    print(n>>1)
    return n ^ (n >> 1)

def mystery_inv(n):
    mask = n >> 1
    while mask != 0:
        n = n ^ mask
        mask = mask >> 1
    return n;

def name_of_mystery():
    return "Gray code"

#def dec_to_bin(num):
#    if num <= 0:
#        return '0'
#
#    bits = ''
#    while num > 0:
#        bits = str(num % 2) + bits
#        num = num / 2
#        
#    return bits
#    
#def bin_to_dec(binary):
#    dec = 0
#    power = 0
#    for b in reversed(binary):
#        dec += int(b) * 2 ** power
#        power += 1
#        
#    return dec
#    
#def mystery(num):
#    b = dec_to_bin(num)
#    out = ''
#    reverse = False
#    for bit in b:
#        if not reverse:
#            out += bit
#        else:
#            out += '0' if bit == '1' else '1'
#            
#        reverse = not reverse if out[-1] == '1' else reverse    
#            
#    return bin_to_dec(out)
#    
#def mystery_inv(num):
#    if num == 0:
#        return num
#
#    b = dec_to_bin(num)
#    out = ''
#    reverse = b[0] == '0'
#    for bit in b:
#        if not reverse:
#            out += bit
#        else:
#            out += '0' if bit == '1' else '1'
#            
#        reverse = not reverse if bit == '1' else reverse
#        
#    return bin_to_dec(out)
#
#def name_of_mystery():
#    return 'Gray code'

""" 
    When you do know almost nothing about bitwise operators except of their existence...
    ...and that you make by chance a good guess... 
"""
#def mystery1(n):  return n ^ (n//2)


"""
    Then you do some pattern recognition to solve the kata! 
"""
#import re, string
#TABLE = string.maketrans('01', '10')

#def mystery_inv(n):
   # return int(''.join( a+b.translate(TABLE)+c for a,b,c in re.findall(r'(1)(0*1?)(0*)', bin(n)[2:]) ) or '0', 2)
    

#def name_of_mystery(): return "Gray code"


g=mystery(7)
h=mystery_inv(7)
print(g,h)
string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+