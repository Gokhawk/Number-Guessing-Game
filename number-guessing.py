from art import logo       # Importing logo from art.py
import random              # Importing random module   

easy = 10           # life values
hard = 5
answer = random.randint(1,100)   # Choosing a number between 1 and 100 with random module 

def compare(number,guess,given_life):    # Defining a function for compare numbers  
    if number > guess:
        print("Too High.")
        return given_life - 1      # If user give a false answer, this will lower user's life 
    elif number < guess:
        print("Too Low.")
        return given_life - 1 
    elif number == guess:
        print(f"You got it. The answer is {answer}")
        return


def user_life():     # Defining a function to choose difficulty and set a life for user
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == "easy":
        return easy
    else: 
        return hard


def number_guess_game ():   # Defining a function for game 
    print(logo)       
    print("Welcome to Number Guessing Game !")
    print("I'm thinking a number between 1 and 100.")
    life = user_life()   # Setting life 

    user_guess = 0  
    while user_guess != answer:
        print(f"You have {life} attempts remaining to guess the number.")    # Showing user how many lifes left 
        user_guess = int(input("Make a guess: "))     # Asking user for a guess 
        life = compare(number=user_guess, guess=answer, given_life=life)    # Comparing user_guess and answer
        if life == 0:   # If user uses all lives. This ends the game
            print(f"The number was {answer}. You Lost.")    
            return
        elif user_guess != answer:     # If user still have lifes, this will continue the game
            print("Guess again.")


number_guess_game()    # Starting the game

