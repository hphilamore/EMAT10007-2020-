#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:11:26 2020

@author: hemma
"""



import math

def MinMax( ListArg ):
    
    Min = math.inf
    Max = -1 * math.inf
    
    for i in ListArg:
        if i < Min:
            Min = i
            
        if i > Max:
            Max = i
            
    return Min, Max

M = MinMax( [1.2, 3.3, 1.6] )

print(M[1])


            
    
            
            






















# def sum_and_increment(a, b):
#     """ Return sum of a and b plus 1 """
#     c = a+b+1
#     d = a
#     return c, d

# d = sum_and_increment(1,2)

# e = sum_and_increment(2,3)

# print(d[0])