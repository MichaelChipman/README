"""
modulo_practice.py
Lesson 7 – Modulo in practice: parity, cycles, positions
Purpose: Demonstrate use of modulo (%) for even/odd checks (parity), cycling patterns, and position finding in repeating sequences.
Author: Michael Chipman
Date: 2025-11-06

Technical concepts demonstrated:
- Modulo Operator (%)
- Parity checks (even/odd using % 2)
- Using modulo to cycle through schedules and repeating groups
- Determining position in a cycle with n % cycle_length
- Boolean expression output (`==` with numbers)
- String formatting with f-strings
- Dynamic borders using "-" * len(string)
- Type checking with type()
"""
# --- Parity (Even/Odd) Checks ---
n = 8
print(n % 2) # Calculates the remainder for parity check (will be 0 for even numbers).
print(type(n % 2)) # Confirms that the modulo result is an integer type.

age = 49
# Uses modulo 2 to create a boolean (True/False) result for even parity.
age_is_even = age % 2 == 0
print(f"age {age} -> even? {age_is_even}")

# --- Cycle and Position Finding ---
day = 23
workers = 5

# Finds the position (remainder) when 23 is divided by 5.
print(23 % 5)

teams = 4
day = 17

# Calculate the index (0-3) of the team that is on duty on day 17.
on_duty = day % teams
print(on_duty) # Display the resulting team index.

# Determine the position of month 7 within a quarterly cycle (cycle length 3).
month = 7
print(month % 3)

shift_length = 4
day = 17

# Calculate the specific shift index (0, 1, 2, or 3) for the given day.
shift = day % shift_length
msg = f"On day {day}, shift {shift} is on duty!"
border = "-" * len(msg)
print(border) # Print dynamic border calculated from the message length.
print(msg)
print(border)

# end modulo_practice.py
