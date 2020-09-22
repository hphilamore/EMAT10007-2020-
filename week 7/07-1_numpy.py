#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:33:45 2020

@author: hemma
"""
import numpy as np


x = [1, 3, 5, 7, 9, 11, 13]

nums = np.array( x )

A = nums[3 : 5]

# ----------------------------------


y = np.array( [ [1,2,3,5,6], 
                [4,5,6,7,8], 
                [7,8,9,9,0] ])

B = y[0, 1]
print(y[1:3, :])


# ----------------------------------

x = np.arange(0, 20)

x = x.reshape(4, 5)





























