# For example, I want to get someones age, I can just ask them, but how does python know it's a question? A question mark won't work...
"""
Little test you can do RIGHT NOW!!! Try to ask whoever runs you code a question, maybe their favourite colour?
"""

# If you used the print() method, as shown in lesson 2, you are close, but that only says stuff.
# Now, for the grand reveal for how to ask a question (And the 2 ways you can acctualy do it)
# The answers are...
# *Drumroll noises*

print("What is your name?")
input()

# Good!!! Now we habve in input, but... does this really do anything? Not really... It just waits for you to do something and then... It does nothing with it.....
# How about I teach you how to make it do something?
# I'm going to make it ask something and make the code remeber it while it runs (anything past that and then we deal with a lot of long learning of some imports

print("What is your name?")
remember_1 = input()
# You can change remember_1 to basicaly anythng you want. I suggest u_name or user_name, or anything like that in this case

# Now, remember lesson 2? I said you can output those variable things... and we just made a variable... So... let's now get to saying that!!!

print("What is your name?")
name = input()

print("Hello, ", name, "!!!") # This is a low level way to join these together, you will see a better way bellow, but stick with this unril you understand it

print(f"Hello, {name}!!!") # This is a better way, and in my opinion the best

"""
That's basicaly all the outputs you could ever need until you get to learing uper se confusing stuff like tkinter, pygame and others
