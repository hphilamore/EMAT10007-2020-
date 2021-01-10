#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:16:33 2020

@author: hemma
"""

# current time
time = 17.05   

work_starts = 8.00
work_ends = 17.00

lunch_starts = 13.00
lunch_ends = 14.00

lunchtime = time >= lunch_starts and time < lunch_ends 

work_time = not(time < work_starts or 
                time > work_ends or 
                lunchtime)

print(lunchtime)

print(work_time)

