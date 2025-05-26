# Juan Rodriguez
# This is a simple program where the system generates a random number and the user has to guess it.
# The system will guide the user to the number until they guess it correctly.

import random 
import time

def main(): # the game
    break_loop = False # flag to break the loop when the user guesses correctly
    attempts = 0 # counter for the number of attempts

    print("Welcome to the Random Proximity Guesser Game!")
    time.sleep(1)
    print("Guess my number, between 1 and 200, and I will tell you how close you are!")
    time.sleep(1)

    num = random_num() # call the function to generate a random number
    while not break_loop:
        guess = guess_num()
        attempts += 1
        if guess == num:
            print(f"Congratulations! You have succesfully guessed {num} on {attempts} tries!")
            break_loop = True
        elif guess < num:
            print(f'Go higher!') 
        elif guess > num:
            print(f'Go lower!')

def random_num(): #generates a random number between 1 and 200
    num = random.randint(1,200)
    return num

def guess_num(): #allows player to guess
    guess = int(input('Guess my number:'))
    return guess


main() #start the game 