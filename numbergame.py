import random

def guess():
    num = int(input("Please enter your guess: "))
    return num

print("Welcome to the number guessing game\n")
print("The objective is to guess the number im thinking of.\n")
print("I will give you clues after your first guess.\n")

secretNumber = random.randint(1,100)

print("I have thought of a number from 1-100\n")

while True: 
    numGuessed = guess()
    if numGuessed < secretNumber:
        print("Guess is too low, guess higher!")
    elif numGuessed > secretNumber:
        print("Guess is too high, guess lower!")
    else:
        print("You guessed it!")
        break
