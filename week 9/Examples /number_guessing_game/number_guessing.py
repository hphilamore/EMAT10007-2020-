#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:47:46 2020

@author: hemma
"""
import numpy as np

print("I'll think of a number between 1 and 20 and you guess what it is")

randNum = np.random.randint(1, 20)
numRounds = 0
foundNum = False

while foundNum == False:
    guessed = int(input("Please guess a number: "))
    if guessed == randNum:
        # print("You win! The number is " + str(randNum))
        foundNum = True
        
    else:
        numRounds += 1
        if guessed < randNum:
            print("You guessed too low!")
        else:
            print("You guessed too high!")
            
print("You win! The number is " + str(randNum))
print("You found the number after " + str(numRounds) + " tries")   
        
            
        
    
    
    

