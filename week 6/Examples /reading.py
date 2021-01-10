#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:54:18 2020

@author: hemma
"""
# file =  open("scores.txt", "r")
# msg = file.read()
# print(msg)
    
    
file =  open("scores.txt", "r")
msg = file.readlines()
print(msg)
words = [line.strip() for line in msg]
print(words)




file =  open("scores.txt", "r")
for line in file:
    print(type(line))