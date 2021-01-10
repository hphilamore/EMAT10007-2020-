#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:07:35 2020

@author: hemma
"""

import random 
from funcs import *

with open('names/first_names.txt', 'r') as first, \
    open('names/last_names.txt', 'r') as last, \
    open('names/movies.txt', 'r') as movies:
    # first = first.read().splitlines()
    # last = last.read().splitlines()
    f = first.read().splitlines()
    l = last.read().splitlines()
    m = movies.read().splitlines()
    for i in range(2):
        
        a = random.randint(0, 20)
        if a < 5:
            movie = m[0]
        elif a < 8:
            movie = m[1]
        elif a < 9:
            movie = m[2]
        elif a < 11:
            movie = m[3]
        elif a < 12:
            movie = m[4]
        elif a < 15:
            movie = m[5]
        else:
            movie = m[6]
        

        text = ""
        text = text + "Name " + random.choice(f) + " " + random.choice(l) + "\n"
        text = text + "Customer number " + "".join([str(r) for r in random.sample(range(10), 10)]) + "\n"
        text = text + "Movie title " + movie + "\n"
        text = text + "Adult " + str(random.randint(0, 5)) + "\n"
        
        if movie==m[0]:
            text = text + "Child " + str(random.randint(0, 5)) + "\n"
        else:
            text = text + "Child " + str(0) + "\n"
        
        text = text + "Concession " + str(random.randint(0, 3)) + "\n"
        
        encrypt
        text = encrypt(random.randint(1, 25), text)
        
        
        with open("sample_data/file_" + str(i) + ".txt", "w") as file:
            file.write(text)
            
        print("")
            
        
        
        
        
        
        
    
        
        
    