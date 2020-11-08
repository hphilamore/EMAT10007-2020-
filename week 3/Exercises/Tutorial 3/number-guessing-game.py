 
#!/usr/bin/env python3
import math
import random
num2guess = random.randrange(1,101)
guess = 0
numofguess = 0
while guess != num2guess:
    print("Enter Your Guess")
    guess = int(input())
    if  guess > 100 or guess < 1:
        print("out of bounds")
    elif guess < num2guess:
         print("Too low")
    else:
         print("Too high")
    numofguess += 1
print("Congratulations it took you", numofguess,"guesses")
#!/usr/bin/env python3
