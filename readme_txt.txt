#========================================================#
#=============> Master Mind from the shell <=============#
#========================================================#

Are you a true fan of the classic game? Have you ever had trouble finding an opponent? 
Fear not! With this python script, you can play against your computer directly from your console!

#======> Design Considerations
The program was written to allow a user to play the game Mastermind with the following rules:

- The sequence can contain pegs of colors: red, yellow, green, blue, white, black.
- A color can be used any number of times in the sequence.
- All four pegs of the secret sequence will contain a color - no blanks/empties are allowed.
- Each guess must consist of 4 peg colors - no blanks.
- The player has 12 guesses to find the secret sequence.

Along the way, I added the following features:

- The program can recognize a couple of common typos, and inform the user when it finds them. 
  These are not counted as a player using a turn.
- A user can specify which colours they would prefer to be used, and the nr. of turns a player has to guess the code.
- If the player has not guessed any colours right, the message "No colours match" will be displayed instead of an empty score

The program is written to work from and run in the shell, as I lack experience in writing GUIs. This is a bit of a shame, 
as Mastermind is a very visual game. A possible improvement I could make if I were to revisit this program would be to see if 
I could at least have the text appear in the console in colour.

Excluding main(), 9 functions are defined in the script of the program. These functions are written to part the script 
into more digestible bites, as well as to avoid repeating code. Most of the text snippets that will, at some point, 
be printed onto the console when the program is running are defined in the beginning of the script, to make it easier to 
correct mistakes or change them entirely. The only exceptions are a couple of f-strings, used in the beginning and the end of 
the game, as I could not find a convenient way to move them to the start of the script.

The program was written for Python 3.11.1, and I cannot guarantee that it will work with another version. 
Aside from the ones mentioned in requirements.txt, the program depends on the built-in modules: sys, random, argparse, and copy.

#======> Repository structure
src: Folder for the python script
- __init__.py
- Master_script.py

github_link.txt: link to github repository
requirements.txt: txt file containing the modules required to run the code
readme_txt: README in a txt file in case the user cannot read the markdown

#======> Usage
The modules listed in requirements.txt should be installed before scripts are run. The code is written for Python 3.11.1.

# network_analysis.py: 
To play the game, run Master-script.py from the repository folder. The script has 3 arguments:

-dv or --dev_cheat: When the argument is called the code secret code will appear underneath the score display
-c  or --colour: The colours used in the game to make codes. Colours should be typed in separated by a space. 
         Keep an eye on how you spell the colours - the way you type them in will be used as a reference 
	 for how the player is scored. You can pick as many or as few colours as you want!
-t  or --max_turns: How many turns a player has to guess the code
-h  or --help: Shows information on how to use the various arguments (the same as wht is written here)

Example of code running the script from the terminal:

python src/Master_script.py -dv -t nr_turns -c colour_1 colour_2 colour_3