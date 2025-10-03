"""
Here we will be doing logic, this is kinda like how games say if you go to 0hp, you die.
"""
# Here we will be doing a simple one where if your name is Bob, you win.

name = input("What is your name?	") # This is from Lesson 3
if name == "Bob":
	print("You win!!!")
else:
	print("You lose.")

"""
== is a "Is this exactly this?". So in line 7, its asking "Is the name Bob? If so do this." but this has a flaw. It has to be EXACTLY Bob. no bob, no BOB, no BOb.
You can also do maths, so 5>2, or 2>=5, etc.
There are a few others like "if 5%2 == 0" which means "is the remainder of 5 divided by 2 0?"
There are a few more but in short, * is times, / is divide, + is add, - is subtract, % is remainder of(Or mod if you want to be technical), // is  division but it then "floors" it, so 15//2 is 7.5, then round down and get 7
Another one is **, which is to the power of. So 10**2 is 100. (10 times 10 = 100)

Another thing is "or". The or means hat it says. We have 2 statments. Think of "Is this person called Bob or is he wearing green? If so, do this."
"and" is similar, both conditions have to be true.
"not" is another one, people ussualy do this one as "!=" which means not equal to. Its like "if Bob isnt wearing green"
"""

# I'm going to ask you to make something where the player is asked some maths thing and if they get it right, they get a point.

"""
One of the ways of doing it are bellow, just prtetend a, b and c are numbers
"""



points = 0
answer = None
a = 1
b = 2
c = a + b
answer = input(f"What is {a} + {b}?")
if answer == c:
	print("You did it!!!")
	points ++ # This djust adds 1 to points. It saves some time rather than writing points = points + 1.
