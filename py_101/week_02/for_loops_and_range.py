"""
for_loops_and_range.py
Lesson 23: For Loops and the Range Function
Purpose: Demonstrates the various ways to use the built-in Python range() function to generate sequences
         for iteration within for loops, including single-argument, two-argument, and three-argument forms.
Author: Michael Chipman
Date: 2025-11-13

Technical Concepts Demonstrated:
- For Loop Iteration (Basic structure)
- Single-Argument Range (Stops before the specified number, starting at 0)
- Empty Range and Loops (range(0) results in zero iterations)
- Two-Argument Range (Specifies start and stop, exclusive of stop)
- Three-Argument Range (Specifies start, stop, and step/increment)
- Negative Step (Counting backward/reverse iteration)
- Loop Accumulation (Calculating sums within a loop)
- Filtering within a Loop (Using an if statement for conditional output)
"""

# ----------- Single-Argument Range -----------
# range(stop): Generates numbers starting from 0, up to, but not including, the stop value (6).
for num in range(6):
    print(num)

# range(1): Executes one iteration (num = 0).
for num in range(1):
    print(num)

# range(0): The stop value is 0, so the loop body is skipped entirely (zero iterations).
for num in range(0):
    print(num)

# ----------- Two-Argument Range -----------
# range(start, stop): Generates numbers starting at 3, up to, but not including, 8.
for num in range(3, 8):
    print(num)

# ----------- Three-Argument Range and Filtering -----------
# range(start, stop, step): Generates even numbers starting at 0, stopping before 11, in steps of 2.
for num in range(0, 11, 2):
    print(num)

# Generates odd numbers starting at 1, stopping before 12, in steps of 2.
for num in range(1, 12, 2):
    print(num)

# Alternative method: Generates all numbers and filters the odds using the modulo operator.
for num in range(1, 12):
    # Check if the remainder when dividing by 2 is 1 (i.e., it's an odd number).
    if num % 2 == 1:
        print(num)

# ----------- Loop Accumulation -----------
# Initialize the accumulator variable outside the loop.
total = 0
# Original summation example (Commented out):
# for n in range(1, 101):
#     total += n
# print(total)

# Accumulates only even numbers: starts at 2, stops before 101, steps by 2.
for n in range(2, 101, 2):
    # Add the current value of n to the running total.
    total += n
print(f"Sum of evens: {total}")

# ----------- Negative Step (Reverse Iteration) -----------
# range(start, stop, step): Starts at 10, stops *before* -1, steps by -1.
for n in range(10, -1, -1):
    print(n)
print("liftoff!")

# ----------- Conditional Output (Complex Filter) -----------
# Iterates from 30 up to, but not including, 51, in steps of 3 (30, 33, 36, 39, 42, 45, 48, 51...).
for n in range(30, 51, 3):
    # Filters: Checks if the remainder when dividing by 10 is 9. This finds numbers ending in 9 (e.g., 39, 49).
    if n % 10 == 9:
        print(n)

# end for_loops_and_range.py
