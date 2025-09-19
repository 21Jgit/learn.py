"""
Outputs in Python can be done in a few ways, you can use the regular print() method
Or you can even use my favourite which uses the sys import
I will go through both methods here, there are more ways, but these are the main 2 that I personaly use
"""

# print() method
print("Hello World!")	# This, when ran, will go to the terminal and say "HEY!!! Say this!"

# (You can also say variables in a print() but we will get to that later.)

# Output with the sys import
"""
You can output whith the import 'sys'
It has a few more lines but can be used to make text be outputed one letter at a time
Bellow is the full code for my one letter at a time idea
"""
import sys
import time
def letters(text, t):
	for k in text:	# This says that for every letter, do this. This is more complex than needed for a simple input, but I use it often enough to put it here, I will explain it in a later lesson.
		sys.stdout.write(k)	# This is saying "HEY!!! Send this out to the terminal!!!"
		sys.stdout.flush() # This is saying "HEY!!! YOYU BETTER SEND THIS OUT!!!", it is more of a failsafe really
		time.sleep(t)	# This is telling the code to wait for some ammount of time
	print()		# This will just make a new line
letters("Hello!!!", 0.05)	# This will say "Hello!!!" 1 letter at a time, one letter every 0.05 seconds


# If you want to just output with sys without anything special, you can do as bellow
import sys
sys.stdout.write("Hello!!!")
sys.stdout.flush()
