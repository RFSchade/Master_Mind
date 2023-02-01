#================================================#
#=============> Master Mind Script <=============#
#================================================#

#=====> Import modules
import sys
import argparse
import random
import pandas as pd
from tabulate import tabulate

#=====> Define global variables
# List of possible colours for the pegs
# (If you change the colours, remember to do it in lowercase)
COLOURS = ["red", "yellow", "green", "blue", "white", "black"]

#=====> Define Functions
# > Get guess from player
def get_guess(colours):        
    # Loop to chack if response is valid
    while True:
        # get input from player
        player_input = input("\nGuess the code: ")
        
        # Clean input
        # Convert to lowercase 
        input_low = player_input.lower()
        # Remove space
        input_clean = input_low.replace(" ", "")
        # Split input into list 
        guess = input_clean.split(",")
        
        # Allow the player to exit the game
        if input_clean == "exit":
            print("_____\n\nGame ended\n_____")
            sys.exit()
        
        # Check if the response contains too few commas
        elif input_clean.count(",") != 3:
            # Check in the player migt have tried to type 'exit'
            if input_clean.count(",") == 0:
                print("_____\n\nd[o_0]b\n\nThis response is invalid! Did you perhaps misspell the 'exit' command?")
                print("Type your response again!")
                continue
            # If not give error message for too few commas
            else:
                print("_____\n\nd[o_0]b\n\nThis response is invalid! It looks like you did not have enough pegs in your guess")
                print("Or perhaps have too many? A valid response should contain 3 commas!")
                print("Type your response again!")
                continue 
        
        # Check if any of the pegs are misspelled
        else: 
            # Define a variable that contains wheter or not the colours of the response match the possible colours
            test = [peg in colours for peg in guess]
            
            # Check if there is a mistake
            if False in test: 
                print("_____\n\nd[o_0]b\n\nThis response is invalid! It looks like you have misspelled one or more of the colours!")
                print("Type your response again!")
                continue
            # Break the loop if all is well
            else: 
                break
    
    # Return the player's guess         
    return guess

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
    
    # Return the player's score
    return score  

# > Display score
def score_dis(turns, guess, score, table):
    # Make guess neater for the display:
    # Capitalize the first letter in guess
    guess_cap = [peg.capitalize() for peg in guess]
    # Unpack guess_cap
    guess_str = ' '.join(str(x) for x in guess_cap)
    
    # I score is empty, define score for no colours
    if not score:
        score_str = "No colours match"
    # If not, unpack score
    else: 
        score_str = ' '.join(str(x) for x in score)
    
    # Add to table
    table.append([turns, guess_str, score_str])
    
    # Print table
    print("_____\n\nd[o_0]b\n")
    print(tabulate(table, headers = 'firstrow', tablefmt = 'fancy_grid'))
    
# > Ask the player if they want to play again
def play_again(colours):
    # Ask the player if they want to play again
    print("\nd[o_0]b\n\nDo you wish to play again?")
    
    while True: 
        # Clean player input
        # get the player's answer
        answer = input("Type 'yes' or 'no': ")
        # Convert to lowercase 
        answer_low = answer.lower()
        # Remove space
        answer_clean = answer_low.replace(" ", "")
        
        # Ask again if the player answers neither yes nor no 
        if answer_clean not in ["no", "yes"]:
            print("\nd[o_0]b\n\nThis response is invalid! Try again")
            continue
        # Close the game if the player answers 'no'
        elif answer_clean == "no":
            print("_____\n\nGame ended\n_____")
            sys.exit()
            break
        # Restart the game if the player answers 'yes'
        elif answer_clean == "yes":
            print("_____\n\nGame restarted\n_____")
            game_fun(colours)
            break   

# > Parse arguments
def parse_args(): 
    # Initialize argparse
    ap = argparse.ArgumentParser()
    # Commandline parameters 
    ap.add_argument("-dv", "--dev_cheat", 
                    required=False, 
                    action=argparse.BooleanOptionalAction,
                    help="When True, shows the code secret code underneath the score display")
    # Parse argument
    args = vars(ap.parse_args())
    # return list of argumnets 
    return args

# > Game Introduction    
def intro(colours):
    # define string of colours
    # Capitalize the first letter fpr each colour
    colours_cap = [colour.capitalize() for colour in COLOURS]
    # Unpack guess_cap
    colours_str = ' '.join(str(x) for x in colours_cap)
    
    # Print intro
    print("_____\n\nd[o_0]b\n\nWelcome to Master Mind! Test your wits, and find out if you are a true Master of the Mind!")
    print("The rules are as follows: I, your opponent will think up a secret code - and you must guess it!")
    print(f"The code will consist of 4 'pegs'. each peg is one of these {len(COLOURS)} colours:\n\n    {colours_str}\n")
    print("Pegs of the same colour can appear multiple times, and each peg will have a colour - no blanks!")
    print("You can give me your guess by typing in the 4 coulours of your choice like this:\n\n    red, red, red, red\n")
    print("Capitalization and spaces are negotiable, but each guess must contain 3 commas, and spelling mistakes will not be tolerated!")
    print("If you are a coward, and wish to end the game, you can type 'exit' at any time.")
    print("Now, let the game begin!\n\n_____")
    
# > Game function
def game_fun(colours):
    # Get argument
    args = parse_args()
    
    # Choose four random colours for the code
    code = [random.choice(colours) for i in range(4)]
    
    # Define variable for the turn nr.
    turns = 1
    
    # Define table
    table = [["Turn", "Guess", "Score"]]
    
    for turn in range(12):
        # Player guess
        guess = get_guess(colours)
    
        # Score
        score = score_guess(guess, code)
    
        # Display score
        score_dis(turns, guess, score, table)
        # Dev cheat 
        if args["dev_cheat"] == True:
            print(code)
        
        # Add to turn nr. 
        turns += 1
        
        # Check if the player has won
        if score == ["Black", "Black", "Black", "Black"]:
            print("_____\n\nd[╥﹏╥]b\n\nI am defeated! you have beaten the game! You are indeed a Master of the Mind!")
            # Ask the player if they want to play again
            play_again(colours)
    
    # Unpack the code so it looks better
    code_str = ' '.join(str(x) for x in code) 
    
    # If the player fails in all 12 turns, give game over message
    print(f"_____\n\nd[✜_✜]b\n\nGame over! Behold, the code you have failed to guess:\n {code_str}")
    # Ask the player if they want to play again
    play_again(colours)

#=====> Define main()
def main():
    # Run game introduction
    intro(COLOURS)
    
    # Run game 
    game_fun(COLOURS) 
    
# Run main() function from terminal only
if __name__ == "__main__":
    main()
