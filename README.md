# Master Mind from the shell
Are you a true fan of the classic game? Have you ever had trouble finding an opponent? Fear not! With this python script, you can play against your computer directly from your console!    

## Repository structure
src: Folder for the python script    
-	\_\_init__.py
- Network_analysis.py

github_link.txt: link to github repository    
requirements.txt: txt file containing the modules required to run the code    

## Usage
Modules listed in requirements.txt should be installed before scripts are run. The code is written for Python 3.11.1.    

__network_analysis.py__     
To play the game, run Master-script.py from the repository folder. The script has 3 arguments:    
- _-dv or --dev_cheat: When the argument is called the code secret code will appear underneath the score display_
- _-c or --colour: The colours used in the game to make codes. Colours should be typed in separated by a space. Keep an eye on how you spell the colours - the way you type them in will be used as a reference for how the player is scored. You can pick as many or as few colours as you want!_
- _-t or --max_turns: How many turns a player has to guess the code_

Example of code running the script from the terminal:    
```
python src/Master_script.py -dv -t nr_turns -c colour_1 colour_2 colour_3
```
