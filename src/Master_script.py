#================================================#
#=============> Master Mind Script <=============#
#================================================#

#=====> Import modules
import sys
import random
import argparse
import copy
#
import pandas as pd
from tabulate import tabulate

#=====> Define texts that appear repeatedly during the game
# input text for retrieving the guess
guess_txt = "\nGuess the code: "

# No colours match 
no_match = "No colours match"

# Character faces
neutral = "[o_0]"
happy = "[⌐■_■]"
sad = "[╥﹏╥]"

# Help text for arguments
dv = "When True, shows the code secret code underneath the score display"
c = "The colours used in the game to make codes. Colours should be typed in separated by a space"
t = "How many turns a player has to guess the code"

# > Lists
# Player ends the game
game_end = ["Game ended"]

# Player restarts game
game_restart = ["Game restarted"]

# 'exit' error message
exit_error = ["This response is invalid! Did you perhaps misspell the 'exit' command?",
              "Type your response again!"]

# Not enough commas error message
comma_error = ["This response is invalid! It looks like you did not have enough pegs in your guess",
               "Or perhaps have too many? A valid response should contain 3 commas!",
               "Type your response again!"]

# Misspelling error message
spell_error = ["This response is invalid! It looks like you have misspelled one or more of the colours!",
                "Type your response again!"]

# Ask player if they want to play again 
again_txt = ["Do you wish to play again?"]

# Error message that appears when player misspells 'yes' or 'no'
quit_error = ["This response is invalid! Try again"]

# Win message
win_txt = ["I am defeated! you have beaten the game! You are indeed a Master of the Mind!"]

#=====> Define Functions
# > Clean input text
def clean_txt(txt):
    # Convert to lowercase 
    txt_low = txt.lower()
    # Remove space
    txt_clean = txt_low.replace(" ", "")
    
    return txt_clean

# > Print strings in format
def show(list_of_str = None, expression = None, end = False, start = True):
    # Define building blacks of the text
    # The text itself
    text_list = copy.copy(list_of_str)
    # Line at the start of a paragraph
    line_start = "_____\n\n"
    # Line at the end of a paragraph 
    line_end = "\n_____"
    # The expression of the character, if one is needed
    if expression == None:
        face = ""
    else:
        face = expression + "\n\n"
    
    # If there is no text, print only a header
    if list_of_str == None:
        print(line_start + face)
    # Ekse print the full text
    else:    
        # Add start_line if needed
        if start == True:
            text_list[0] = line_start + face + text_list[0]
        elif start == False:
            text_list[0] = "\n" + face + text_list[0]
        
        # Add end line if needed
        if end == True:   
            text_list[-1] = text_list[-1] + line_end
            
        # Print all items on the text list
        for text in text_list:
            print(text)
            
# > Game Introduction    
def intro(colours):
    # define string of colours
    # Capitalize the first letter for each colour
    colours_cap = [colour.capitalize() for colour in colours]
    # Unpack guess_cap
    colours_str = ' '.join(str(x) for x in colours_cap)
    # Define 
    intro_text = ["Welcome to Master Mind! Test your wits, and find out if you are a true Master of the Mind!",
                  "The rules are as follows: I, your opponent will think up a secret code - and you must guess it!",
                  f"The code will consist of 4 'pegs'. each peg is one of these {len(colours)} colours:\n\n    {colours_str}\n",
                  "Pegs of the same colour can appear multiple times, and each peg will have a colour - no blanks!",
                  "You can give me your guess by typing in the 4 coulours of your choice like this:\n\n    red, red, red, red\n",
                  "Each guess must contain 3 commas, and misspelled words will not be tolerated!",
                  "If you are a coward, and wish to end the game, you can type 'exit' at any time.",
                  "Now, let the game begin!"]
    
    # Print intro
    show(intro_text, expression = neutral, end = True)
            
# > Get guess from player
def get_guess(colours):        
    # Loop to chack if response is valid
    while True:
        # get input from player
        player_input = input(guess_txt)
        
        # Clean input
        input_clean = clean_txt(player_input)
        # Split input into list 
        guess = input_clean.split(",")
        
        # Allow the player to exit the game
        if input_clean == "exit":
            show(game_end, end = True)
            sys.exit()
        
        # Check if the response contains too few commas
        elif input_clean.count(",") != 3:
            # Check in the player migt have tried to type 'exit'
            if input_clean.count(",") == 0:
                show(exit_error, expression = neutral, start = False)
                continue
            # If not give error message for too few commas
            else:
                show(comma_error, expression = neutral, start = False)
                continue 
        
        # Check if any of the pegs are misspelled
        else: 
            # Define a variable that contains wheter or not the colours of the response match the possible colours
            test = [peg in colours for peg in guess]
            
            # Check if there is a mistake
            if False in test: 
                show(spell_error, expression = neutral, start = False)
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
        score_str = no_match
    # If not, unpack score
    else: 
        score_str = ' '.join(str(x) for x in score)
    
    # Add to table
    table.append([turns, guess_str, score_str])
    
    # Print table
    show(list_of_str = None, expression = neutral)
    print(tabulate(table, headers = 'firstrow', tablefmt = 'fancy_grid'))
    
# > Ask the player if they want to play again
def play_again(colours, args):
    # Ask the player if they want to play again
    show(again_txt, expression = neutral, start = False)
    
    while True: 
        # Clean player input
        # get the player's answer
        answer = input("Type 'yes' or 'no': ")
        # Clean answer
        answer_clean = clean_txt(answer)
        
        # Ask again if the player answers neither yes nor no 
        if answer_clean not in ["no", "yes"]:
            show(quit_error, expression = neutral, start = False)
            continue
        # Close the game if the player answers 'no'
        elif answer_clean == "no":
            show(game_end, end = True)
            sys.exit()
            break
        # Restart the game if the player answers 'yes'
        elif answer_clean == "yes":
            show(game_restart, end = True)
            game_fun(colours, args)
            break   

# > Parse arguments
def parse_args(): 
    # Initialize argparse
    ap = argparse.ArgumentParser()
    # Commandline parameters 
    ap.add_argument("-dv", "--dev_cheat", 
                    required=False, 
                    action=argparse.BooleanOptionalAction,
                    help=dv)
    ap.add_argument("-c", "--colours", 
                    required=False, 
                    type=str,
                    default=["red", "yellow", "green", "blue", "white", "black"],
                    nargs="+",
                    help=c)
    ap.add_argument("-t", "--max_turns", 
                    required=False, 
                    type=int,
                    default=12,
                    help=t)
    # Parse argument
    args = vars(ap.parse_args())
    # return list of argumnets 
    return args
    
# > Game function
def game_fun(colours, args):
    
    # Choose four random colours for the code
    code = [random.choice(colours) for i in range(4)]
    
    # Define variable for the turn nr.
    turns = 1
    
    # Define table
    table = [["Turn", "Guess", "Score"]]
    
    for turn in range(args["max_turns"]):
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
            show(win_txt, expression = sad)
            # Ask the player if they want to play again
            play_again(colours, args)
    
    # Unpack the code so it looks better
    code_str = ' '.join(str(x) for x in code) 
    
    # If the player fails in all 12 turns, give game over message
    show([f"Game over! Behold, the code you have failed to guess:\n {code_str}"], expression = happy)
    # Ask the player if they want to play again
    play_again(colours, args)

#=====> Define main()
def main():
    args = parse_args()
    # Get adn clean colours
    use_colours = [clean_txt(colour) for colour in args["colours"]]
    
    # Run game introduction
    intro(use_colours)
    
    # Run game 
    game_fun(use_colours, args) 
    
# Run main() function from terminal only
if __name__ == "__main__":
    main()
