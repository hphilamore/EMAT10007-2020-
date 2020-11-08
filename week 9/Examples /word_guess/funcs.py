#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:11:57 2020

@author: hemma
"""
import random 
from string import ascii_lowercase


def get_num_tries():
    attempts = 0
    #while(attempts < 1 or attempts > 25):
    while(not(1 <= attempts <= 25)): 
        attempts = int(input("How many tries do you want? "))
    return attempts

def get_random_word():
    with open('wordlist.txt', 'r') as f:
        words = f.read().splitlines()
        word = random.choice(words)
        #print(word)
    return word

def print_state(tries, wrong, gaps):
    print(f'Attempts remaining: {tries}')
    W = ' '.join(wrong)
    print(f'previous guesses: {W}')
    disp_word = ''.join(gaps)
    print(disp_word)