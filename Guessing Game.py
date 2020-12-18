import random

#We have to have the computer generate a random number
iCompNum = random.randint(1, 100)

#This boolean is our exit condition for the while loop
bHasGuessed = False

while not bHasGuessed:
    #Takes in user input and prompts them
    iPlayerGuess = input("Enter a number from 1 to 100: ")

    #Chhecking if we are >, < or ==
    if iPlayerGuess == iCompNum:
        print("You're correct! The final answer was: ", iCompNum)
        break
    elif iPlayerGuess > iCompNum:
        print("You guessed too high.")
    else:
        print("You guessed too low.")

#Done with the project

