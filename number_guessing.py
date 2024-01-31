import random
import os
import sys


def guess_a_number():
    difficulty = input("Do you want to play in hard or easy mode?(H = hard, E = easy)")
    guesses = 10 if difficulty.lower() == "e" else 5
    number_to_guess = random.randint(1, 101)
    
    print("Number to guess", number_to_guess)
   
    play(guesses, number_to_guess)
    play_again()
    
    
    
def play(guesses, number):
    user_guess = int(input("GUESS A NUMBER\n"))
    this_game_number = number
    if user_guess != number and user_guess > number:
        print("TRY LOWER")
        play(guesses, this_game_number)
    elif user_guess != number and user_guess < number:
        print("TRY HIGHER")
        play(guesses, this_game_number)
    elif user_guess == number:
         print("You guessed right")

    

def play_again():
    play_again = input("Do you want to play again? (Y/N)")
    if play_again.lower() =="y":
        clear_screen()
        guess_a_number()
    else:
        print("You have exited the game. BYE")



def clear_screen():
    os.system("cls")


mygame = guess_a_number()