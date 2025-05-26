# Juan Rodriguez
# This program is a simple game where the user must guess a random number from a certain range
# chosen by the system.

import random
import time

def main():
    break_loop = False #flag to break the loop when the user guesses correctly

    print("Welcome to the Random Guessing Game!")
    time.sleep(1)
    print("I have selected a random number between 1 and 10.")
    time.sleep(1)
    print("If you guess it correctly, you win!")

    num = random_num() #call the function to generate a random number

    while not break_loop:
        guess = guess_num()
        if guess == num:
            print("Congratulations! You guessed the number correctly!")
            break_loop = True
        else:
            print("Sorry, that's not correct. Try again!")
            time.sleep(1)
    print("Thanks for playing!")

def random_num():
    #generate a random number between 1 and 10
    num = random.randint(1,10)
    return num

def guess_num():
    #ask the user to guess
    guess = int(input("Please enter your guess: "))
    return guess

main() #start the game


# while it is not necessary to do this in blocks of functions, I am just doing it to 
# make it more readable and organized

# I am familiarizing myself with the use of functions and booleans in Python