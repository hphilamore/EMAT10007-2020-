#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:54:55 2020

@author: hemma
"""

# DEFAULT ARGUMENTS

def func(message):
    print(message)
    

def func2(message, copies=2):
    for c in range(copies):
        print(message) 
        
def func3(message, copies=2, name="Hemma"):
    for c in range(copies):
        print(message + " " + name)
        
# func2("hi", 3)

func3("hi", name="Tim")


# --------------------------------------

# MULITPLE ARGUMENTS

def SumItems( ListArg ):
    sum = 0
    for i in ListArg:
        sum += i
    print(sum)
    

def SumItems2(*Args, A=3):
    sum = 0
    for i in Args:
        sum += i
    print(sum)
    
    

L = [2, 3, 4, 5]

SumItems( L )


SumItems2(3, 5, 6, 4, A=3)

# --------------------------------------

# SCOPE

def SomeFunction(number):
    age = 25
    print(age, number, name)
    return age

name = "Hemma"

Age = SomeFunction(4)

# --------------------------------------


def print_string():
    global text
    text = 2
    #print(text)
    

print_string()

print(text)





























































































