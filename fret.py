#!/usr/bin/python3
import re
from collections import deque

intro = """
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
"""

def main():
	print(intro)
	chromatic = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
	tune_prompt = input('Are you in standard tuning? Y/N ')
	affirmative = re.compile('(y|yes)', re.IGNORECASE)
	
	if re.match(affirmative, tune_prompt):
		string = input('String? ')
		for i in chromatic:
			if i == string:
				start = chromatic.index(i)
				if start != 0:
					start = start * -1 #convert to negative for reversing rotate method later
				else: start = 0

		fret = input('Fret? ')
		try:
			intTest = int(fret)
		except ValueError:
			print('We\'re not going to get into microtones here.')
		fret = int(fret)
		while fret > 12:
			fret = fret - 12		
		chromatic = deque(chromatic)
		chromatic.rotate(start) 
		note = chromatic[fret]	
		print(note)
	
	else:
		print('Alternate tunings are not currently available, Mr. Fancypants.')
		print('Go play in American Football.')

if __name__ == "__main__": main()