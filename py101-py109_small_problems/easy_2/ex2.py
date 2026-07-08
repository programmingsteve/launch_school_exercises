# Write a program that asks for user's name, then greets the user. If the user
# appends a ! to their name, the computer will yell the greeting (print it
# using all uppercase).

# Example 1
# What is your name? Sue
# Hello Sue.

# Example 2
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

def greet(name):
   greeting = "Hello " + name
   if name.endswith("!"):
       return(greeting.upper() + " WHY ARE WE YELLING?")
   else:
       return(greeting + ".")

name = input("What is your name? ")
print(greet(name))
