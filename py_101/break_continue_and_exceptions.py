"""
break_continue_and_exceptions.py
Lesson 25: Break, Continue, and Robust Input
Purpose: Demonstrates how the 'break' and 'continue' statements alter loop execution flow, 
         and how to combine 'while True' with exceptions for creating robust input loops.
Author: Michael Chipman
Date: 2025-11-13

Technical Concepts Demonstrated:
- Infinite Loop (while True)
- Break Statement (Immediate loop exit)
- Continue Statement (Skip remaining body, move to next iteration)
- Looping with Sentinel Value (quit)
- Skip Logic (Skipping even numbers)
- Exception Handling (try/except)
- Input Validation Loop (Robust number entry)
- Accumulation with Loop Control
"""

# ----------- Break Example (Infinite Loop with Exit) -----------
# The 'while True' creates a permanent loop, relying on 'break' to exit.
# while True:
#     word = input("Type a word")
#     # If the sentinel value is entered, the 'break' immediately terminates the entire loop.
#     if word == "quit":
#         break
#     else:
#         print(f"You typed {word}")

# ------------------ Continue Example (For Loop Skip) -----------
# This loop is designed to print only the odd numbers from 1 to 10.
# for n in range(1, 11):
#     # If the number is even, the 'continue' immediately skips the rest of the loop
#     # body and moves execution directly to the next iteration (n + 1).
#     if n % 2 == 0:
#         continue
#     print(n)

# ------------------ Continue: Dead Code Illustration -----------
for n in range(1, 10):
    if n % 2 == 0:
        # The 'continue' statement prevents any code written below it in this block
        # from ever being executed on this iteration.
        continue
        print("this doesn't print") # This line is 'dead code'
    print(n)

# ------------------ Accumulation with Continue -----------
# sum = 0
# for n in range(1, 11):
#     # Skips adding even numbers to the accumulator.
#     if n % 2 == 0:
#         continue
#     # Only odd numbers reach the accumulation step.
#     sum += n
# print(sum)

# ------------------ Combined Break and Continue Example -----------
# word = input("Enter word or type 'quit' to exit")

# while True:
#     word = input("Enter word or type 'quit' to exit")
#     if word == "quit":
#         # Exits the loop entirely.
#         break
#     elif word == "":
#         # Skips the print statement and jumps to the next iteration (asking for input again).
#         continue
#     else:
#         print(word)

# ------------------ Basic Exception Handling (Quick Reference) -----------
# The 'try' block attempts the code that might fail (casting non-number input).
# try:
#     x = int(input("Type a number: "))
#     print("You typed:", x)
# # If the code fails with a ValueError (e.g., typing 'hello' instead of 12),
# # execution moves immediately to the 'except' block.
# except ValueError:
#     print("That wasn’t a valid integer.")

# ------------------ Robust Input Loop (Break, Continue, Try/Except) -----------
# Accumulator variable.
total = 0
# 'while True' guarantees the loop runs until a specific 'break' is hit.
while True:
    try:
        x = input("Type a number (or 'stop'): ")
        if x == "":
            # Skips the rest of the body if input is empty, asking again.
            continue
        elif x == "stop":
            # Prints the total and exits the infinite loop.
            print(total)
            break
        else:
            # Attempts to cast the input to a float and add it to the total.
            x = float(x)
            total += x
    # If the user types text (and it wasn't 'stop'), the ValueError is caught.
    except ValueError:
        print("Invalid input")

# end break_continue_and_exceptions.py
