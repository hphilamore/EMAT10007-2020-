#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:46:49 2020

@author: hemma
"""


# LISTS

student_list = [ ["John", 68, False], 
                  ["Sarah", 75, True], 
                  ["Mary", 95, True] ]

student_list.append( ["Kent", 70, True] )

# print(student_list[0])

for entry in student_list:
    for sub_entry in entry:
        print(sub_entry)


#----------------------------------

# LIST COMPREHENSION

xRange = [x+1 for x in range(5)]

y = [3 * x * x + 5 for x in xRange]

matrix = [[x, x**2, x**3] for x in xRange ]

for row in matrix:
    print(row)
    
#----------------------------------
0.001

t = [x/1000 for x in range(10)]

#----------------------------------

evenNr = [x for x in range(10) if x%2==0]

#----------------------------------


names = ["mia", "Tom", "Zara"]

# MIA = "mia".upper()

# print(MIA)

upper = [x.upper() for x in names]

#----------------------------------

numbers = [3, 0, 2, 10, 7]
low = [x for x in numbers if x <= 5]

#----------------------------------

# SETS

first_set = {1, 2, 3, 4, 4, 5}

second_set = {1, 2, 2, 7, 8}

print(3 in second_set)

print( first_set - second_set )

print( first_set | second_set )

print( first_set & second_set )

print( first_set ^ second_set )

# first_set[1] # ERROR - sets are unordered

#----------------------------------

# DICTIONARY

states = { "Oregon" : "OR" ,
           "Florida": "FL",
           "California": "CA",
           "New York": "NY"
           }

states["Michigan"] = "MI"

del states["New York"]

# print(states.keys())

# print(states.values())

# print( sorted(states.keys()) )

print(states.items())


for key, val in states.items():
    print(key)
    print(val)
    print()
    




































































