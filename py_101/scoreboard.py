# scoreboard.py
# Simple Python scoreboard display with custom border
# Author: Michael Chipman
# Date: 2025-11-04
#
# TECHNICAL CONCEPTS DEMONSTRATED:
# - Variable Assignment (String & Integer Data Types)
# - f-String Formatting (String Interpolation)
# - Output (print() function)
# - String Manipulation (Concatenation '+', Repetition '*' operators)
# - Built-in Function (len() for calculating string length)
# - Effective Code Commenting
#
# For portfolio/github: demonstrates a professional approach to foundational code.

# Store current player name
player = "Ace"

# store current player score
score = 42

# store the output message
msg = f"Player {player} Score {score}"

# Print top border
# '╔' (Top-Left) + '═' repeated + '╗' (Top-Right)
print('╔' + '═' * (len(msg) - 5) + '╗')

# print output message with border
print(f'║   {msg}   ║')

# print bottom border
print('╚' + '═' * (len(msg) - 5) + '╝')

# end-scoreboard
