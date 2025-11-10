"""
if_else_mental.py
Lesson 2 week 2 lesson to learn If/else: syntax, indentation, mental model
Author: Michael Chipman
Date: 2025-11-09

Technical Concepts Demonstrated
- How Python uses indentation to define which code runs after if and else.
- Writing if/else statements with comparison operators (==, !=, <, >, <=, >=).
- The difference between = (assign a value) and == (check for equality).
- Using % for checking if a number is even or odd.
- Printing with f-strings for money formatting, like f"{price:.2f}".
- How to import random and use random.randint() to get a random integer.
"""
# ------- Broken if statement ----------
x = 5
if x == 5:
    # Error demonstration: The print statement runs even if x is not 5 due to missing indentation.
    # Indentation for if or else code blocks must be exactly 4 spaces.
    print("x is five") # fixed version (unindent for error)

# ------ basic if/else structure -----------

# temp = 70 # prints 'Comfortable'
temp = 80 # prints 'Too hot'
if temp > 75:
    print("Too hot")
else:  # else: starts on same indentation as if:. It only runs if the 'if' condition is False.
    print("Comfortable")

# ------- if/else exercise --------

age = 12 # store age

if age < 18:
    # If the customer is under 18, set the price to 7 (child rate).
    price = 7
else:
    # If the customer is 18 or older, set the price to 12 (adult rate).
    price = 12

print(f"{price:.2f}")

# ------- is number even/odd program ------------
# Import the random module to generate random integers
import random
# Generate a random number between 1 and 100
num = random.randint(1, 100)

if num % 2 == 0:
    # The Modulo operator (%) returns 0 for even numbers.
    print("even")
else:
    # The number is odd if the remainder is not 0.
    print("odd")

# end if_else_mental.py
