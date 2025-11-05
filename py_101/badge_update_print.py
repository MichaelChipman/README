# badge_update_print.py
# Python demo: compound assignment and comma-based expression printing
# Author: Michael Chipman
# Date: 2025-11-04
#
# TECHNICAL CONCEPTS DEMONSTRATED:
# - Variable Assignment & Reassignment (“same box, new value”)
# - Compound Assignment Operators (+=, -=)
# - print() with comma-separated arguments (auto-spacing)
# - Mixing text and expressions in print()
# - Handling Floating-Point Imprecision using round()

# store the initial score value
score = 10

# Compound Assignment: Use += to increment score by 4 (score is reassigned from 10 to 14).
score += 4

# Print the current value of score
print(score)

# store the initial price
price = 20

# Compound Assignment: Raise price by 5 using the += operator
price += 5

# Compound Assignment: Reduce the price by 3 using the -= operator
price -= 3

# Print the final value in price
print(price)

# Floating Point Imprecision Issue:
# This happens because many decimal fractions (base 10), like 0.7 or 0.1,
# cannot be represented perfectly as finite fractions in the computer's binary (base 2) system.
# The calculation uses the closest binary approximation, causing slight inaccuracies.
print("Final price is", price * 1.07)

# Solution for Currency:
# Use the round() function to control decimal precision.
# round() takes two arguments: the expression and the number of digits (ndigits) to round to.
print("Final price is", round(price * 1.07, 2))

# end badge_update_print.py
