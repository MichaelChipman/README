"""
balance_board.py
Stretch challenge for Lesson 4: tracks cash withdrawals, prints balance with a dynamic border.
Author: Michael Chipman
Date: 2025-11-05

Technical concepts demonstrated:
- Variable assignment and compound assignment (+=, -=)
- Arithmetic expressions in print()
- print() with commas (auto-spacing)
- Dynamic borders with len() and string repetition
- Chaining multiple compound assignments for transaction log style
"""

# store cash value
cash = 50

# simulate 3 withdraws using compound assignment -=
cash -= 4
cash -= 3.50
cash -= 4.50

# Store output message
# NOTE: Using commas for assignment creates a 'tuple' (msg).
# msg = "Cash left:", cash, "USD" 

# Design Rationale for Border Sizing:
# Because 'msg' is a tuple, len(msg) returns the item count (3), not the character length.
# We must create a dedicated string (border_size) to accurately calculate the required border length.
# The cash value is explicitly converted to a string (cash_str) to allow concatenation,
# and manual spaces are included to match the auto-spacing behavior of comma-printing.
# store cash as a string for len()
cash_str = str(cash)
border_size = "Cash left: " + cash_str + " USD"
border = "@" * len(border_size)

# print a border and the msg
print(border)
print("Cash left:", cash, "USD")

# end balance_board.py
