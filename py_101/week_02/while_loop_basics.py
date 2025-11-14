"""
while_loop_basics.py
Lesson 24: While Loop Basics and Sentinel Values
Purpose: Demonstrates the fundamental structure of the while loop, focusing on the need for a
         clear Boolean condition, a loop body, and a crucial update (or sentinel) variable to
         prevent infinite loops.
Author: Michael Chipman
Date: 2025-11-13

Technical Concepts Demonstrated:
- While Loop Structure (Condition, Body, Update)
- Preventing Infinite Loops (Necessity of the update step)
- Loop Counter (Counting down)
- Sentinel Value (User input controlling loop execution)
- Loop Accumulation (Calculating sums)
- Input Function (Getting user data)
"""

# ----------- Basic Countdown Loop -----------
# Initialize the loop control variable (condition start).
count = 10
# The loop continues to execute as long as the condition (count >= 0) is True.
while count >= 0:
    print(count)
    # CRITICAL: The update step. Decrementing the counter ensures the condition
    # eventually becomes False, preventing an infinite loop.
    count -= 1

# --------------- Sentinel-Controlled Loop -----------
# Initial prompt/read of the sentinel variable.
response = input("Please type quit: ")
# The loop executes as long as the user's input does NOT match the sentinel value ("quit").
while response != "quit":
    print(response)
    # Update step: Re-prompting the user is necessary to potentially change
    # the sentinel variable and terminate the loop.
    response = input("Please type quit: ")

# --------------- Accumulation with While Loop -----------
# Initialize the counter variable (start).
numbers = 1
# Initialize the accumulator variable (total).
sum_total = 0
# The loop executes as long as the counter is within the desired range.
while numbers <= 10:
    # Accumulation: Add the current counter value to the running total.
    sum_total += numbers
    # Update step: Increment the counter to ensure the loop terminates.
    numbers += 1
# The final result is printed outside the loop body.
print(f"This is the sum {sum_total}")

# end while_loop_basics.py
