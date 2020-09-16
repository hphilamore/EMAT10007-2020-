#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:47:47 2020

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
    
    def __add__(self, other):
        cd = self.den * other.den
        cn = self.num*other.den + other.num*self.den
        return( MyFraction(cn, cd) )

fractionA = MyFraction(3,4)
fractionB = MyFraction(4,3)
added = fractionA + fractionB
print(added)












# print(float(fraction))
    


# print( float(fraction) + 0.2)





# print(fraction)









# print(fraction.eval())

# x = 1

# print( eval('x + 1') )

# print(fraction.num)

# fraction.normalize()

# print(fraction.num)
# fractionB = MyFraction(3, 4)
# print(fractionB.num)

























# import math

# class MyFraction():
#     def __init__(self, num, den):
#         self.num = num
#         self.den = den
        
# fraction = MyFraction(1, 2)

# print(fraction.num)






