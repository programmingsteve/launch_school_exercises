# Build a program that randomly generates and prints Teddy's age. To get the
# age, you should generate a random number between 20 and 100, inclusive.

# Example Output
# Teddy is 69 years old!

import random

# age = random.randint(20, 100)
# print(f"Teddy is {age} years old!")

# Further Exploration

# Modify this program to ask for a name, then print the age for that person.
# For an extra challenge, use "Teddy" as the name if no name is entered.

age = random.randint(20, 100)
name = input("Enter a name: ") or "Teddy"
print(f"{name} is {age} years old!")
