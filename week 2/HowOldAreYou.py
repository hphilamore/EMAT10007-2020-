"""This is a program to demonstrate simple string input and
conditionals based on strings"""

yourAge = input("How old are you? ")

if int(yourAge) < 15:
    print("You must be a genius!")
elif int(yourAge) < 101:  # which is between 15 and 100
    print("I think", str(yourAge) + " is a fine age!")
else:
    print("Wow! Your are more than 100. Impressive!")
print("Bye for now.")

# Note that the test for checking whether two values are equal to one another
# is written with *two* equals signs, i.e. "==".

# Note the different ways of joining strings together inside a print statement.

# Note the elif statement means "else if".

# Note the print at the end gets executed no matter which condition is
# true/false, because it is not indented and, hence, not part of the
# conditional block.

