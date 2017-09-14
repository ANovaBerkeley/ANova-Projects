import sys
from colorama import init, Fore, Back, Style

"""Truck ASCII art taken from: http://www.chris.com/ascii/index.php?art=transportation/trucks""" 

"""

This section lets python read an ASCII art input file
"""
input_file = open("sampleArt.txt", "r")
text = input_file.read()


"""

This command lets the computer know that we want to use 'colorama' to use colors in the terminal
"""
init()


"""

This function lets us create text and highlight colors. 

'Foreground' refers to font color
'Background' refers to highlight color

"""

def cprint(foreground, background):
    style = getattr(Fore, foreground) + getattr(Back, background)
    return (style, Style.RESET_ALL)

"""

This function lets us choose which color to use when we print to the terminal. 
Notice how we use ord() to find the integer representation of each character.
Then we use if-statements to determine which color we'll use.

The function returns a couple of things: a string that says which colors to use
and a string that resets the colors in the terminal.

Colors that you can use:

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

"""

def pickColor(character):

	character = ord(character)

	if character >= 0 and character < 32:
		fontcolor = "RED"
	if character >= 32 and character < 64:
		fontcolor = "YELLOW"
	if character >= 64 and character < 96:
		fontcolor = "BLUE"
	if character >= 96 and character < 129:
		fontcolor = "GREEN"

	bgcolor = "BLACK"
	return cprint(fontcolor, bgcolor)


"""

This section prints a string containing all the characters from the ASCII art file and their corresponding colors

"""
result = ""
for letter in text:
	result += pickColor(letter)[0] + letter + pickColor(letter)[1]
print(result)

