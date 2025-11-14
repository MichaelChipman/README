"""
logical_operations_demo.py
Lesson 18: Logical Operators and Short-Circuiting Demo
Purpose: Demonstrates how to use 'and', 'or', 'not' in Python and how short-circuit evaluation works.
Shows practical examples with conditionals, boolean logic, and output.
Author: Michael Chipman
Date: 2025-11-10

Technical Concepts Demonstrated:
- Use of logical operators: 'and', 'or', 'not'
- Truth tables and boolean conditions
- Short-circuit evaluation in Python (where the second operand is skipped)
- Writing clean conditional statements
- Using f-strings for output
- Basic use of random number generation
"""

# -------- Shows how 'and' works ----------

# The 'and' operator requires BOTH conditions to be True to return True.
# age = 22
# has_ticket = False
# print(age > 18 and has_ticket) # Result: False (True AND False)

# ------ Shows how 'or' works ---------

# The 'or' operator requires only ONE condition to be True to return True.
# age = 15 # Condition 1: False (age is not >= 18)
# with_parent = True # Condition 2: True
# if age >= 18 or with_parent == True: # If one condition returns True, access is granted
#     print("access granted")

# --------- Shows how 'not' works ----------

has_key = False # Current state is False
door_is_locked = not has_key # 'not' flips the boolean value, resulting in True
print(door_is_locked) # prints True

# -------- Demo: short-circuiting ----------

def right():
    """Prints a message and returns True."""
    print("right side evaluated")
    return True

# print(False and right()) # Short-circuited: prints False since the first condition is False (right() not called)
# print(True or right()) # Short-circuited: prints True since the first condition is True (right() not called)
# print(True and right()) # Not short-circuited: right() is called since 'and' needs to check the second condition
# print(False or right()) # Not short-circuited: right() is called since 'or' needs to check the second condition

# -------- Demo: short-circuiting (Simplified Repetition) ----------

# This section repeats the short-circuit concept using simpler comments for clarity.
def right():
    """Prints a message and returns True."""
    print("right side evaluated")
    return True

# print(False and right()) # prints False since the first condition is False
# print(True or right()) # prints True since first condition is True
                        # In both these cases, the right() function is not executed due to short-circuiting.
# print(True and right()) # To run right() with 'and', the first condition must be True.
# print(False or right()) # To run right() with 'or', the first condition must be False.

# ---------- Demo: short-circuiting with compound conditions ---------
import random  # Imports the 'random' library for number generation
temp = random.randint(50, 100) # Generates a random integer for temperature between 50 and 100

# Compound Condition: Picnic is possible if (Temp is above 70 AND even) OR if Temp is above 90.
if (temp > 70 and temp % 2 == 0) or temp > 90:
    print(f"Picnic possible! temp = {temp}°F") # Prints if the full compound condition is True
else:
    print(f"No picnic possible! temp = {temp}°F") # Prints if the full compound condition is False

# end logical_operations_demo.py
