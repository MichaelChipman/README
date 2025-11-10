"""
identity_vs_equality.py
Lesson 19: Identity (is) vs. Equality (==)
Purpose: Demonstrates the crucial difference between checking for value equality (==) and object identity (is).
Author: Michael Chipman
Date: 2025-11-10

Technical Concepts Demonstrated:
- Value Equality (==): Compares the values of two objects.
- Object Identity (is): Compares the memory addresses (IDs) of two objects.
- Literal cache and string interning behavior in Python.
- Floating-point imprecision and the need for rounding.
- Boolean aliases and internal representation.
"""

# ----------- Boolean identity -----------
# flag = True              # Assigns flag to the boolean singleton True
# print(flag)              # Outputs the value (True)
# print(flag is True)      # Checks if flag refers to the exact same object as True (always True)

# ----------- Boolean equality -----------
# print(True == 1)         # Checks value equality: True (Booleans have numerical equivalents)
# print(True is 1)         # Checks identity: False (True is a bool object, 1 is an int object)

# ----------- Float precision -----------
# x = 0.1 + 0.2          # x suffers from floating-point imprecision
# y = 0.3                # y is a precise float literal
# x = round(x, 1)        # Fixes x to 0.3, allowing value equality check to pass
# print(x == y)          # Value check: True after rounding
# print(x is y)          # Identity check: False (different memory locations)

# ----------- Compound identity -----------
# num = 42               # num holds the value 42
# alias = num            # alias refers to the SAME object as num (identity holds due to integer caching)

# if num % 2 == 0 and alias is num: # Checks value (even) AND identity (same object)
#     big_even = True
# else: 
#     big_even = False

# print(big_even)

# -------- String identity --------

a = "hello"
b = "hel" + "lo"
print(a == b)  # value equality (True)
print(a is b)  # identity (False, because 'b' is constructed at runtime and not interned)

# end identity_vs_equality.py
