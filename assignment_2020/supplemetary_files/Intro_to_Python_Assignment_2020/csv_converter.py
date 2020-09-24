#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:18:59 2020

@author: hemma
"""
#https://www.w3schools.com/python/ref_string_split.asp#:~:text=The%20split()%20method%20splits,number%20of%20elements%20plus%20one.
with open('douglas_data.csv') as infile, open('douglas_data.txt', 'w') as outfile:
    for line in infile:
        outfile.write(" ".join(line.split(sep=',')).replace(',', ''))
        #outfile.write(",") # trailing comma shouldn't matter