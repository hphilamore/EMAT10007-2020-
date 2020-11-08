import matplotlib.pyplot as plt
import numpy as np


# simple plot with list
plt.plot([1,2,3,4],'go')
plt.show()


# add bits and pieces
plt.plot([1,2,3,4],'go')
plt.plot([0.5,3,4,6],'r')
plt.title("Our first plot")
plt.xlabel("time")
plt.ylabel("numbers")
plt.text(2, 0.65, 'Just some text')
plt.grid()
plt.show()



# Some more interesting  data
a = np.arange(0,3, .02)
b = np.arange(0,3, .02)
c = np.exp(a)  # exponential
d = -1*np.exp(a)    #

fig = plt.figure(7)
plot1 = plt.plot(a, c, 'b', label='$y=e^t$')
plot2 = plt.plot(a, d, 'g', label='$y=e^{-t}$')

plt.legend()
plt.show()


# how to make subplots

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')


plt.show()

# checkout link for example plots and corresponding code
# https://matplotlib.org/1.3.1/gallery.html

