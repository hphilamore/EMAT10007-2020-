#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:35:56 2020

@author: hemma
"""

# SAVE A PLOT


import matplotlib.pyplot as plt
import numpy as np
import csv 



x = [-1, 3, 4, 8, 10]

y = [-1, 2, 5, 6, 7 ]

plt.plot(x, y)

plt.savefig("my_plot.png")

# ------------------------------------------------------

# IMPORTING DATA

data_path = 'signal_data.csv'

with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = np.array(list(reader)).astype(float)

print(data)

# plot the data
plt.plot(data[0, :], data[1, :])

# ------------------------------------------------------

# BAR PLOT EXAMPLE 

data_path = 'temperature_data.csv'

with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)

print(data)

cities = [d[0] for d in data[1:]]
data = [d[1:] for d in data]
headers = data[0]
data = np.array(data[1:]).astype(float)

# 1. array with x-ticks
x_pos = np.arange( data.shape[1] )

# width of bars
W = 0.2

# 2. bar plot 
#for i in range(3):
for i in range(data.shape[0]):
    plt.bar(x_pos, data[i, :], width=W, label=cities[i])
    x_pos = x_pos + W
    
# 3. replace x ticks
plt.xticks(x_pos-W, headers, rotation=30)

# 4. legend
plt.legend()

# ------------------------------------------------------

# IMPORTING USING NUMPY

data = np.loadtxt('temperature_data.csv', delimiter=',', 
                  skiprows=1, usecols=range(1,7))

# ------------------------------------------------------


data = np.genfromtxt('temperature_data.csv', delimiter = ',', 
                     usecols=range(1,7), names=True)


print(data['Jul'])
























































































