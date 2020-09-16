#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:53:17 2020

@author: hemma
"""

# RECURSIVE FUNCTIONS

def pow(x, n):
    if(n == 1):
        return( x )
    else:
        return x * pow(x, n-1)
    
A = pow(2, 5)



def Factorial( Num ):
    if Num == 0:
        return 1
    else:
        return(Num * Factorial( Num - 1))
    
A = Factorial(3)
        























