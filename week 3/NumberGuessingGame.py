import random

GuessedNumber = int(input("Please guess a number from 1-10: "))

ChosenNumber = random.randint(1,10)

while GuessedNumber != ChosenNumber:
    # If the number guessed was larger...
    if ... :
        GuessedNumber = int(input("Incorrect, ...: "))
    # If the number guessed was smaller...
    elif ... :
        GuessedNumber = int(input("Incorrect, ...: "))

print("Success! You guessed correctly, the number was: ", ChosenNumber)