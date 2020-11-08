#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:35:55 2020

@author: hemma
"""

import matplotlib.pyplot as plt
import numpy as np
import csv 
from scipy.optimize import curve_fit

# FIT A POLYNOMIAL FUNCTION 

x = [2.105263157894736725e+00, 3.157894736842105310e+00,4.210526315789473450e+00, 5.263157894736841591e+00, 6.315789473684210620e+00,0.000000000000000000e+00, 1.052631578947368363e+00, 7.368421052631578760e+00,8.421052631578946901e+00,9.473684210526315042e+00,1.052631578947368318e+01,1.157894736842105132e+01,1.263157894736842124e+01,1.894736842105263008e+01,2.000000000000000000e+01,1.368421052631578938e+01,1.473684210526315752e+01, 1.578947368421052566e+01,1.684210526315789380e+01,1.789473684210526372e+01]
y = [7.445192947240600745e+01, 4.834835792411828947e+01, 6.873305436340778840e+01, 5.979576407972768948e+01,6.404530772390434379e+01,6.090548420541189500e+01, 7.157546008677115879e+01, 8.620253336570679892e+01, 1.138154622045899913e+02, 8.493639813028174501e+01, 9.783457330550828601e+01, 1.082064229481453594e+02, 1.063876210674365979e+02, 1.001971993955305038e+02, 1.061496321788094832e+02, 1.279575585921491836e+02, 1.556956405962417875e+02, 1.584164804859289859e+02, 1.753888794716459358e+02, 1.980941276403034124e+02]

tmp = sorted(zip(x, y))

x = [t[0] for t in tmp]
y = [t[1] for t in tmp]

#plt.plot(x, y)

coeffs = np.polyfit(x, y, 3)

yfit3 = np.poly1d(coeffs)(x)

plt.scatter(x, y)
plt.plot(x, yfit3)

# ---------------------------------

# FIT AN ARBITRARY FUNCTION


data_path = 'signal_data.csv'

with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = np.array(list(reader)).astype(float)

x = data[0, :]
y = data[1, :]

plt.scatter(x,y)
plt.show()

def fit_sin(x, a, b, c, d):
    y = a * np.sin(b*(x+c)) + d
    return y

opt, cov = curve_fit(fit_sin, x, y)

yfit = fit_sin(x, *opt)

plt.scatter(x, y)
plt.plot(x, yfit)



# ---------------------------------

# FIT AN ARBITRARY FUNCTION WITH MULTIPLE VARIABLES 

def func(X, a, b):
    x,y = X
    z = a*x + b*y**2
    return z

x = np.linspace(0.1, 1.1, 101)
y = np.linspace(1.0, 2.0, 101)
a = 1
b = 2
z = func((x, y), a, b) 
plt.scatter(x, z)
z = z + np.random.random(101)
plt.scatter(x, z)

opt, cov = curve_fit(func, (x, y), z)
zfit = func((x, y), *opt)
print(opt)
plt.plot(x, zfit)




















































