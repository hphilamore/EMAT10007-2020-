#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:51:14 2020

@author: hemma
"""

# FOR LOOPS

x = ["Hemma", "Ben", "Jay"]

for y in x: 
    print( "Name is " + y )
    
# -------------------------------

y = [2, 4, 6]

for Y in y:
    print(Y + 1)
    
# -------------------------------

for i in range(2, 31, 2):
    print(i)
    
# -------------------------------

w = "Hello"

for char in w:
    print(char)
    
# -------------------------------

for i in range(10):
    if i%2 == 0:
        print(i)
    else:
        print("-")

# -------------------------------

# WHILE LOOPS

w = ["Hemma", "Ben", "Jay"]

print(len(w))

index = 0

while index < len(w):
    print(w[index])
    index += 1
    
# -------------------------------

stop = "Ben"

while w[index] != stop:
    print(w[index])
    index += 1

# -------------------------------

Num =0

while Num < 20:
    print(Num)
    Num = Num + 2
    
print("That's enough!")

# -------------------------------

seq = ["Hemma", "Ben", "Jay", "Lara", "Mia"]

for var in seq:
    if var == "Jay":
        continue
    print(var)
    
print("finished")











        
    
    
    
    
    
    
    
    
    
    
    
    




