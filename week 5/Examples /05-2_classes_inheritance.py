#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:25:42 2020

@author: hemma
"""
import math

class MyFraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.normalize()
        
    def normalize(self):
        gcd = math.gcd(self.num, self.den)
        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)
    
    def eval(self):
        return(self.num / self.den)
    
    def __float__(self):
        return(self.num / self.den)
    
    def __str__(self):
        return (" " + str(self.num) + "\n---\n" + " " + str(self.den) + "\n")








class NamedFraction(MyFraction):
    
    def __init__(self, num, den, name):
        super().__init__(num, den)
    
    def sig_fig(self, n):
        return round(super().eval(), n)
        # return round(self.eval(), n)
    
    def eval(self):
        return self.num + self.den

nfrac = NamedFraction(2, 3, "two thirds")

print( nfrac.sig_fig(3))

print( nfrac.eval() )




    
    


















































    