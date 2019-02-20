#!/usr/bin/python3
import re
from collections import deque

def main():
	intro()
	run_program()

def run_program():
	string_finder()
	continue_prompt()
		
def string_finder():
	#variables
	chromatic_natural = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
	chromatic_flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
	chromatic_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] 		
	natural_input = re.compile('(a|b|c|d|e|f|g)', re.IGNORECASE)
	flat_input = re.compile('(bb+|eb+|ab+|db+|gb+|cb+|fb+)', re.IGNORECASE)
	sharp_input = re.compile('((f#)|(c#)|(g#)|(d#)|(a#)|(e#)|(b#))', re.IGNORECASE)
	#initial prompt
	string = input(
	"""
What string are you playing?
(Note: Use b for flats and # for sharps.)
""")
	#match input with natural, sharp, or flat scale and find note
	if re.match(flat_input, string):
		scale = chromatic_flat
		start = find_start(scale, string)
		note_finder(start, scale)
	
	elif re.match(sharp_input, string):
		scale = chromatic_sharp
		start = find_start(scale, string)
		note_finder(start, scale)
		
	elif re.match(natural_input, string):
		scale = chromatic_natural
		start = find_start(scale, string)
		note_finder(start, scale)
				
	else:
		print('That\'s not a string.')

def find_start(scale, string):
	for i in scale:
		if i == string:
			start = scale.index(i)
			if start != 0:
				start = start * -1 #convert to negative for reversing rotate method in note_finder()
			else: start = 0
			return start

def note_finder(start, scale):
	fret = input('Fret? ')
	try:
		intTest = int(fret)
	except ValueError:
		print('We\'re not getting into microtones here.')
	fret = int(fret)
	while fret >= 12:
		fret = fret - 12		
	scale = deque(scale)
	scale.rotate(start) 
	note = scale[fret]	
	print('That\'s a {}'.format(note))
		
def continue_prompt():
	continue_prompt = input('Need to check another note? Y/N ')
	affirmative = re.compile('(y|yes)', re.IGNORECASE)
	if re.match(affirmative, continue_prompt):
		run_program()
	else:
		print('\nKeep shredding \m/')

def intro():
	print(
		"""
              ,
             { \\
            {   `\\
           {  .-'`"'--.
          {.'       00 \\
         /`    /\\_______")
        /  ((  \\ \\/\\/\\/\\/
       /        `^^^^/
      |           '/{`\\
      | |        `/{__|
      |  \\   \\.-'//,
       \\  \\   | // |
        \\  \\___\\/.'
         | |  // \\ 
        /  /\\ ` _/
       /  (  ```
     .'    '.
    /__/V\\___\\ Welcome to Guitar Center
""")
	
		
if __name__ == "__main__": main()