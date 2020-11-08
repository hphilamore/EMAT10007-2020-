# We will use this later as an explanation
import sys
import time

def FibRecursive(n):
	"""
	The first way I'm going to write the Fibonacci function is with
	a really exciting technique that uses RECURSION.
	That is, a function calls itself within its definition.
	"""

	# First we deal with the special cases i.e. if n == 1 or 2
	if n == 1 or n == 2:
		# Notice we are returning values, not printing them.
		# Returning a value is necessary as we use the result
		# of one call to FibRecursive() to calculate the result of
		# another call to FibRecursive().
		return 1
	elif n > 2:
		# Fib(n) = Fob(n - 1) + Fib(n - 2)
		# So here we make a call to the function we're currently writing!
		# Eventually, it reaches the special cases above, because either
		# n == 1 or n == 2. In either case we return 1.
		return (FibRecursive(n - 1) + FibRecursive(n - 2))

for i in range(1,15):
	print(FibRecursive(i), end="  ")
print()
print()

# Great, so this works! But what if we call it on a large value of n?
print("Calling Fib() on a large number will take a long time, and the recursive version can produce a \"stack overflow\" error on machines with little available memory.")
RecursiveStart = time.time()
print(FibRecursive(35))
RecursiveEnd = time.time()

print()

"""
Typically, Python sets a recursion limit to avoid causing the stack to overflow. If you're interested in learning more about why stack overflows occur, please google it as you will find plenty of information on a site called... stack overflow!
For example, your machine has the current recursion limit set by Python:
"""
print("Current recursion limit: " + str(sys.getrecursionlimit()))
print()

# Notice that it either takes forever to calculate an answer, or, more likely,
# Python eventually throws a Stack Overflow exception, meaning it has called
# too many functions within functions within functions
# (due to our use of recursion) to return a value without exceeding its memory
# restrictions. Is there a better way?

# The imperative way - this can be a little difficult, do not worry if it doesn't
# make sense at first, it's not crucial.

def FibImperative(n):
	# set the default values for n = 3, our starting, non-special case
	previous = 1
	current = 1
	# handle the special cases
	if n == 1 or n == 2:
		return 1
	elif n > 2:
		# If n is 1 or 2, return 1, otherwise we go from 3 .. n
		for i in range(3,n):
			# set next to be equal to the next result for
			# (Fib(n - 1) + Fib(n - 2))
			next = previous + current
			# then update previous for the next iteration of the loop
			previous = current
			# and, similarly, update current for the next iteration of the loop
			current = next
		return next


for i in range(1,15):
	print(FibRecursive(i), end="  ")
print()
print()

# Great, so this works! But what if we call it on a large value of n?
print("Typically, the imperative version should be a little faster than the recursive version... but not always by much. Is it worth using recursion for the simplicity?")

ImperativeStart = time.time()
print(FibRecursive(35))
ImperativeEnd = time.time()

"""
We use recursion when we know we're not dealing with too many recursive calls, because it makes the code very simple, compact and readable. It can also be much easier to write than the imperative version.
"""

print("Recursive version took {0:.2f} seconds.".format(RecursiveEnd - RecursiveStart))
print("Imperative version took {0:.2f} seconds.".format(ImperativeEnd - ImperativeStart))
