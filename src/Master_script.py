#================================================#
#=============> Master Mind Script <=============#
#================================================#

#=====> Import modules
import sys
import random
import pandas as pd
from tabulate import tabulate

#=====> Define Functions
# > Generate a code
def generate_code():
    # Define list of colours
    colours = ["red", "yellow", "green", "blue", "white", "black"]
    
    # Choose four random colours
    code = [random.choice(colours) for i in range(4)]
    
    return code

# > Get guess from player
def get_guess():    
    # get guess from player
    guess = input("Guess the code: ")
    if guess == "exit":
        print("Game ended")
        sys.exit()
    # Remove space
    guess_no_space = guess.replace(" ", "")
    # Split guess into list 
    guess_list = guess_no_space.split(",")
    
    return guess_list

# > Calculate a score for a guess
def score_guess(guess, code):
    # Define empty list for the score
    score = []
    
    # > Calculate score:
    # Loop for Black score  
    for i, j in zip(guess, code):
        if i == j:
            score.append("Black")
        elif i in code:
            score.append("White")
    
    # Sort score
    score.sort()
    
    return score  

# > Display score
def score_dis(guess, score):
    # Unpack the guess and score so they look better
    guess_str = ' '.join(str(x) for x in guess)
    score_str = ' '.join(str(x) for x in score)
    
    # Define table
    table = [["Guess", "Score"], [guess_str, score_str]]
    
    # Print table
    print("d[o_0]b")
    print(tabulate(table, headers = 'firstrow', tablefmt = 'fancy_grid'))
    
# > Game function
def game_fun():
    # Generate code
    code = generate_code()
    
    for turn in range(12):
        # Player guess
        guess = get_guess()
    
        # Score
        score = score_guess(guess, code)
    
        # Display score
        score_dis(guess, score)
        # dev cheat 
        print(code)
        
        if score == ["Black", "Black", "Black", "Black"]:
            print("_____\n d[o_0]b Congratulations, you have beaten the game! Do you whish to play again? \n_____")
            answer = input("Type 'yes' or 'no': ")
            
            if answer == "no":
                sys.exit()
            elif answer == "yes":
                game_fun()
    
#=====> Define main()
def main():
    
    game_fun()    

# Run main() function from terminal only
if __name__ == "__main__":
    main()
