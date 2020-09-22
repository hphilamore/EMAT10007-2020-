#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:41:13 2020

@author: hemma
"""

import matplotlib.pyplot as plt


x = [-1, 3, 4, 8 , 10]
f = [-1, -2, 7, 13 , 1]

plt.plot(x, f)
plt.show()

#-------------------------------

plt.plot(x, f, '-xr');
#plt.plot(x, f, '--og')  
plt.plot(x, f, 'og--')  
plt.plot(x, f, 'or--') 
plt.plot(x, f, 'k.') 
plt.show()

#-------------------------------

plt.subplot(211)    # 2 rows, 1 column, index 1
plt.plot(x, f, 'r')

plt.subplot(212)    # 2 rows, 1 column, index 2
plt.plot(x, f, 'b--')

plt.show()

#-------------------------------

plt.subplot(221)    # 2 rows, 2 columns, index 1
plt.plot(x, f, 'r')

plt.subplot(222)    # 2 rows, 2 columns, index 2
plt.plot(x, f, 'b')

plt.subplot(223)    # 2 rows, 2 columns, index 3
plt.plot(x, f, 'r--')

plt.subplot(224)    # 2 rows, 2 columns, index 4
plt.plot(x, f, 'b--')
plt.show()
#-------------------------------

plt.plot(x, f, '-xr', linewidth=6, markersize=15);
plt.show()
#-------------------------------

plt.plot(x, f, '-xr', label="data 1")

# Legend
plt.legend(loc='best', fontsize=12)

# Axes labels
plt.xlabel('$x$', fontsize=20)
plt.ylabel('$f$', fontsize=20)

# Title
plt.title("Simple plot of $f$ against $x$", fontsize=18);

plt.show()



#-------------------------------
import matplotlib.pyplot as plt
import numpy as np

num_points = 100
x = np.linspace(0, 4*np.pi, num_points)
f = np.sin(x)

plt.plot(x, f);

# Use the start and end values in x as x limits 
plt.xlim(x[0], x[-1])

# Label axis
plt.xlabel('$x$')
plt.ylabel('$\sin(x)$')

plt.show()

#-------------------------------

x = [-1, 3, 4, 8 , 10]
f = [-1, -2, 7, 13 , 1]


plt.plot(x, f)
plt.xlim(x[0], x[-1])
plt.show()


#-------------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.array(x)
f = np.array(f)

plt.plot(x, f, label='f')
plt.plot(x, f**2, label='f^2')
plt.legend()
plt.show()

x = [-1, 3, 4, 8, 10]
y = [-1, -2, 7, 13, 1]

plt.plot(x, y, '--xr', 
          linewidth=3, 
          markersize=15, 
          label='data')

# legend
plt.legend(loc='best', fontsize=12)

# axes labels
plt.xlabel('x', fontsize=15)
plt.ylabel('f', fontsize=15)

# title
plt.title("plot of x vs f", fontsize=15)

plt.show()]


# -------------------------------------------

year_groups = ['B1', 'B2', 'B3', 'M1', 'M2']
num_students = [500, 332, 425, 300, 200]

# 1. create an arry with posiytion of x ticks
x_pos = np.arange((len(year_groups)))


# 2. bar chart
plt.bar(x_pos, num_students)

# 3. replace x ticks with year group name
plt.xticks(x_pos, year_groups)

# 4. axis labels
plt.xlabel('year group')
plt.ylabel('number of students')

# -------------------------------------------

import matplotlib.pyplot as plt

x = [-1, 3, 4, 8, 10]
y = [-1, -2, 7, 13, 1]

plt.plot(x, y)

plt.xlim(x[0], x[-1])

plt.show()

# -------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = [-1, 3, 4, 8, 10]
y = [-1, -2, 7, 13, 1]


#plt.plot(x, y, 'ko')
plt.scatter(x, y)

# -------------------------------------------

x = [-1, 3, 4, 8, 10]
y = [-1, -2, 7, 13, 1]

plt.subplot(221)
plt.plot(x, y, 'r')


plt.subplot(222)
plt.plot(x, y, 'm')

plt.subplot(223)
plt.plot(x, y, 'k')

plt.subplot(224)
plt.plot(x, y, 'c')












































































































