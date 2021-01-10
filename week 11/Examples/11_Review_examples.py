# Q.11.1.A

# a) An increasing population is when the number of new emigrants and 
# the number of deaths is less than the number of new immigrants and 
# the number of births. 
emigrants = 4
deaths = 3
immigrants = 2
births = 1

pop_increase = (emigrants + deaths) < (immigrants + births)
print(pop_increase)

# b) Draw two counters of the same colour from a bag of blue and green 
# counters to win the game. 
C1a = 'B'
C1b = 'B'
C2a = 'B'
C2b = 'G'

win = (C1a == C1b) and not(C2a == C2b)
print(win)

# --------------------------------------------------------------------------

# Q.11.2.A

p = float(input("Amount in GBP (£): "))

m = 1.36

if p<= 100:
    f = 0.9
elif 100 < p <= 1_000:
    f = 0.925
elif 1000 < p < 10_000:
    f = 0.95
else:
    f = 0.97
    
r = p * m * f

print(r)

# --------------------------------------------------------------------------

# Q.11.2.B
# Write a program that prints all the integers from 0 to 6 inclusive, using a loop.  

for i in range(7):
	print(i)

# --------------------------------------------------------------------------

# Q11.2.C
# Write a program that prints every second element of a list, using a loop.

my_list = [1, 2, 3, 4, 5, 6]

for i in my_list[1::2]:
	print(i)

# --------------------------------------------------------------------------

# Q.11.2.D
# Write a program that requests a number from the user until the number input 
# by the user is greater than 10. 
number = 0
while(number <= 10):
	number = float(input("Input a number: "))

# --------------------------------------------------------------------------

# Q.11.2.E
# Write a program that prints all the integers from 0 to 6 inclusive, except 3 and 4, using a loop.  
# (Modify your answer to Q.11.1.B)


for i in range(7):
	if i == 3 or i == 4:
		continue
	print(i)

# --------------------------------------------------------------------------

# Q.11.2.F
# Write a program that prints every element of a list of numbers, using a 
# loop, exiting te loop before printing the number if a number greater than 10 
# is reached.

my_list = [1, 2, 13, 4, 5, 6]

for i in my_list:
	if i > 10:
		break
	print(i)


# --------------------------------------------------------------------------

# Q.11.3.A
# Write a function, is_even.   
# Input: n (integer)
# Output: True if n is even, False if n is not even

def is_even(n):
	
	# Using control statements
	# if n%2:
	# 	return False
	# else:
	# 	return True

	# Using logic
	return not n%2 

print(is_even(1))


# --------------------------------------------------------------------------

# Q.11.3.B
# Write a function to calculate gravitational potential energy of an object:

# Input: m (mass), g (acceleration due to gravity), h (height) 
# Output: gravitational potential energy, E = mgh

m = 1 # kg
g = 9.81 # ms^-2
h = 10 # m

def E(m, g, h):
	return m*g*h
	#return f"E = {mgh} J"

print( E(m, g, h) )

# --------------------------------------------------------------------------

# Q.11.3.C
# a) Write a function to calculate gravitational potential energy of an 
# object, assuming g=9.81ms-2 .
# (Rewrite your answer to Q11.1.B)
m = 1 # kg
h = 10 # m

def E(m, h, g=9.81):
	return m*g*h
	#return f"E = {mgh} J"

print( E(m, h) )

# b) a) Write a function to calculate gravitational potential energy of 
# an object of mass 1kg, assuming g=9.81ms-2.

m = 2 # kg
h = 10 # m

def E(h, m=1, g=9.81):
	return m*g*h
	#return f"E = {mgh} J"

print( E(h) )
print( E(h, 2) )

# --------------------------------------------------------------------------

# Q.11.3.D
# Write a function to find the magnitude of an n-dimensional vector
import numpy as np

def magnitude(*args):
	#return np.sum((np.asarray(args)**2))**0.5
	return np.sqrt(np.sum((np.asarray(args)**2)))

print(magnitude(0,2,5))

# --------------------------------------------------------------------------

# Q.11.4.A 
# Create the numpy array:
# 	  [[6,    8,   10], 
#      [12, 14, 16],
#      [18, 20, 22]]

m = np.arange(6, 23, 2).reshape(3,3)
print(m)

# --------------------------------------------------------------------------

# Q.11.4.B 
# Find sin(x) for each value, x, in the list:  [𝜋/2, 𝜋, 𝜋/4]
n = [np.pi/2, np.pi, np.pi/4]

# --------------------------------------------------------------------------

# Q.11.4.C
# Add [6, 4, 2] to each row of the array in your answer to Q.11.4.A to get:
#  	  [[12,    12,   12], 
#      [18,    18,   18],
#      [24,    24,   24]]
p = m + [6, 4, 2]
print(p)

# --------------------------------------------------------------------------

# Q.11.4.D
# Find the dot product of the four elements in the upper left corners of the 3x3 arrays in Q.11.4.A and Q.11.4.C  
m_ = m[:2,:2]
p_ = p[:2,:2]
print( np.dot(m_, p_) )

# --------------------------------------------------------------------------

# Q.11.4.E 
# Create a line plot of row 1 against row 0 of the numpy array: 
# 	  [[6,    8,   10], 
#      [18, 20, 22]]

import matplotlib.pyplot as plt 

data = np.array([[6, 8, 10], [18, 23, 12]])

plt.plot(data[0], data[1])

plt.show()

# --------------------------------------------------------------------------

# Q.11.4.F 
# Create a scatter plot of the exponential function, e^x, for 𝑥 in the range 0 to 10 inclusive. 

f = np.arange(11)
g = np.exp(f)

plt.scatter(f, g)

plt.show()

# --------------------------------------------------------------------------

# Q.11.5.A
# Write a Python class which has two methods:
# get_String : request string from user and assign value to class attribute
# print_String : print the string in upper case


class My_class():

	def __init__(self):
		pass
		#self.my_string = 'None'

	def get_string(self):
		self.my_string = input("input some text: ")

my_object = My_class()
my_object.get_string()
print(my_object.my_string)

# --------------------------------------------------------------------------
# Q.11.5.B
# Write a Python class, square_analyser which:
# is constructed using a single input argument, s (length of one side). 
# has two methods:
# 	area : prints the area of the square
# 	perimeter : print the area of the square 
class Square_analyser():
	def __init__(self, h):
		self.h = h

	def area(self):
		print(self.h**2)

	def perimeter(self):
		print(self.h*4)

square = Square_analyser(5)
square.area()
square.perimeter()




# Q.11.5.C
# Write a child class, Rectangle_analyser, inherited from Square_analyser 
# (Q.11.5.B), that is constructed using two input variables: height, width 
# and has two methods:
# 	area : prints the area of the rectangle
# 	perimeter : prints the perimeter of the rectangle
class Rectangle_analyser( Square_analyser ):
	def __init__(self, h, w):
		super().__init__(h)
		self.w = w

	def area(self):
		print(self.h*self.w)

	def perimeter(self):
		print( 2*self.h + 2*self.w )

rectangle = Rectangle_analyser(3, 4)
rectangle.area()
rectangle.perimeter()


