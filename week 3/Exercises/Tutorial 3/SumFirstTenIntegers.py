# Program for summing the first n numbers,
Sum = 0

for i in range(11):
	# Sum up only even numbers by using the modulo operator.
	# The "modulo" operator applied to two numbers returns the "modulus", or
	# the remainder of a division. In this example, we know that a number is
	# even if the modulus of x % 2 == 0.
    if (i % 2 == 0):
        print(i)
        Sum = Sum + i
        # We can also rewrite this in a shorthand form as the following:
        # Sum += i
        # Where += is equivalent to "x = x + y" or, to put it another way,
        # += is to take the current value and increase it by 1, as opposed to x = 1
        # which would simply reassign x to equal 1. Similar contractions of operators
        # include -=. *= and /=.
print("==")
print(Sum)

# Exercise: Change the summation so that we only sum the odd numbers, rather than even numbers.
