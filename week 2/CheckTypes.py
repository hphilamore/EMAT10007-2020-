# This program checks the type of variable Var and prints
# it out to the user in a human friendly way

Var = 1

if(type(Var)==int):
    print (Var," is an integer.")
elif(type(Var)==float):
    print (Var," is a float.")
elif(type(Var)==complex):
    print (Var," is a complex number.")
elif(type(Var)==str):
    print (Var," is a string.")
elif(type(Var)==bool):
    print (Var," is a boolean.")
else:
    print("hmmm... I'm not sure what that is!")

# Notice that `elif' is equivalent to nesting multiple `if-then-else' statements,
# `elif' is just a contraction of `else-if' such that we can save on extra indentation
# by combining the `else' line with `if ... then'. It produces shorter, more readable
# code without additional indentation levels, which would otherwise be
# unavoidable in Python.

# Exercise: change the value of Var to test all the different types.
# Try and define Var as a list. How can you fix the program to check for lists?


