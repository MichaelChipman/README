"""
modeling_real_world_calculations.py
Lesson 5: Practice translating word problems into code and clear outputs.
Author: Michael Chipman
Date: 2025-11-05

Technical concepts demonstrated:
- Translating word problems into arithmetic expressions
- Doing arithmetic inside print() for usable output
- Comparing clarity of print() formats (commas, parentheses)
- Dynamic borders using len() and string repetition
- Tuple vs string issues in assignment and printing
- Explicit str() casting with +
"""

# Demo: answer to Maestro's word problem
print("Total with tax is", 24 * (1 + 0.07))

# comparing two print statements
print("Total with tax is", 24 + 24 * 0.07)
print("Total with tax is", 24 * 1.07) # is direct and clear.

# Word problem: concert tickets
# Ticket cost and quantity for word problem
ticket = 56
num_tickets = 3

# Dynamic border, matches message length, print message under border
print("*" * len("I spent " + str(ticket * num_tickets) + " Dollars"))
print("I spent " + str(ticket * num_tickets) + " Dollars")

# reviewing commas in assignment vs string +
msg = "Hi", 7       # Tuple
print(type(msg))    # <class 'tuple'>
print(len(msg))     # Number of items in tuple
print(type(msg[0])) # <class 'str'> first item in tuple
print(len(msg[0]))  # Length of first tuple item
print(type(msg[1])) # <class 'int'> second item in tuple
# len(msg[1]) would fail (no length for int)

# TypeError demo and fix
# print("Answer: " + ticket * num_tickets) # This would error
print("Answer: " + str(ticket * num_tickets)) # Fixes the error

# end modeling_real_world_calculations.py
