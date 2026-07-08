# Build a program that displays when the user will retire and how many years
# she has to work till retirement.

# Example
# What is your age? 30
# At what age would you like to retire? 70
#
# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

from datetime import date

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
years_until_retirement = retirement_age - age
current_year = date.today().year
retirement_year = current_year + years_until_retirement

print(
    f"It's {current_year}. You will retire in {retirement_year}.\n"
    f"You have only {years_until_retirement} of work to go!"
)
