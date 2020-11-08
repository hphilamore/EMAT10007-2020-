#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:59:46 2020

@author: hemma
"""

Days = ["Mon", "Tue", "Wed"]

Days.append("Thu")

Days.append("Sat")

Days.insert(4, "Fri")

print(Days)

# Days.remove("Tue")

# del Days[1]

# thursday = Days.pop(3)

# print(Days)

# print(thursday)

# Days = []

# print(Days)

# print( Days.index("Wed") )

# print( Days.count("Wed") )

Days[1] = 'Tuesday'

print(Days)

