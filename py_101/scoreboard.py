# scoreboard.py
# Simple Python scoreboard display with custom border
# Author: Michael Chipman
# Date: 2025-11-04
# For portfolio/github: demonstrates print(), comments, and formatting

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
print(f'║   {msg}   ║')

# print bottom border
print('╚' + '═' * (len(msg) - 5) + '╝')

# end-scoreboard
