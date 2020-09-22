# Little number guessing game
# Guess a random number between 1 and 100
import random

print("I think of a number between 1 and 100 and you will have to guess it")

# get a random number between 1 and 100
randNum = random.randint(1,100)
numRounds = 0
foundNum = False

while foundNum == False:
    numRounds = numRounds + 1
    guessedNum = input("Please guess a number: ")
    if int(guessedNum) == randNum:
        print("You found the number!")
        foundNum = True
    else:
        if int(guessedNum) < randNum:
            print("My number is bigger!")
        else:
            print("My number is smaller!")

print("Congratulations! You found the number in " + str(numRounds) + " rounds!")

# Go to the Python console
# import random
# Have a look at the description of the function random.randrange()
# What does it do?
# Try out different values.
# What does the "step" do?
# Note that [ ] in the function description means that it is an optional parameter,
# i.e., the function uses a default parameter


# What are other functions in the random module? – use "dir (random)"


# Make sure the user only types a number that is between 1 and 100
# and give the user feedback if that's not the case.

# Consider what might be the most efficient way to guess a number between 1 and 100. It is important to try and think about it algorithmically, and how you might break the process down into discrete steps.
# Look up "binary search" on Wikipedia and try to understand how you might guess the numbers according to this algorithm (no need to implement it yourself).
