#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:08:29 2020

@author: hemma
"""

from string import ascii_lowercase
import random

def get_num_attempts():
    attempts = 0
    while(not(1 <= attempts <= 25)):
        attempts = int(input("How many tries do you want? "))
    return attempts


def get_random_word():
    with open ('wordlist.txt', 'r') as f:
        words = f.read().splitlines()
        word = random.choice(words)
        print(word)
    return word
    

# specify difficulty
tries = get_num_attempts()

# select random word
word = get_random_word()

# game state variables
gaps = [False for letter in word]
wrong = []
remaining = set(ascii_lowercase)
word_solved = False

# main game loop    
while(tries > 0 and not word_solved):
    
    print(f'attempts remaining: {tries}')
    W = ' '.join(wrong)
    print(f'previous guesses: {W}')
    disp_word = ''.join([l if gaps[n] else '*' for n, l in enumerate(word)])
    print(disp_word) 
    
    # get next letter guess 
    next_l = input('Choose the next letter: ').lower()
    
    # check if letter in word
    if next_l in word:
        # guess correct
        print(f'{next_l} is in the word!')
        for i in range(len(word)):
            if word[i] == next_l:
                gaps[i] = True
                
        if False not in gaps:
            word_solved = True

                
    # guess incorrect
    else:
        print(f'{next_l} is not in the word!')
        tries -= 1
        wrong.append(next_l)
        
        
print(f'The word is {word}') 

if word_solved:
    print('congratulations, you won!')
else:
    print('try again next time')
         
        

    
    