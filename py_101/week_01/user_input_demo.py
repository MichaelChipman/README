"""
user_input_demo.py
Lesson 9: "Talking to your program: getting input from users"
Purpose: Demonstrate user interaction by capturing input and performing calculations based on that data.
Author: Michael Chipman
Date: 2025-11-6

Technical Concepts:
- input(): Standard function for retrieving user data (always returns a string).
- Explicit Type Casting: Using int() and float() to convert string input to usable numeric types.
- Arithmetic Expressions: Performing calculations with user-provided numbers.
- round(): Function for controlling floating-point precision.
- f-string Formatting: Displaying results cleanly with dynamic borders.
"""

# Prompt user for a name; input() always returns a string.
user_name = input("Please enter your first name!")
print("Hello", user_name)

# Prompt for age and immediately cast the string input to an integer (int).
user_age = int(input("What is your age?(whole number like 23)"))
print(user_age)

# Commented out block: Demonstrates type inspection and simple arithmetic.
# print(type(user_age))
# print("Next year you'll be", user_age + 1)

# Commented out block: Demonstrates casting to float for price and complex financial formatting.
# price = float(input("What is the price?"))
# quantity = int(input("What is the quantity purchased?(whole number like 3)"))
# subtotal = price * quantity
# print(subtotal)
# msg = f"total due $ {round(subtotal, 2):.2f}"
# border = "-" * len(msg)
# print(border)
# print(msg)
# print(border)

# --- Test Score Average Calculation ---

# Input first score, casting the string result to integer.
tScore1 = int(input("Please enter your first test score(0 to 100)"))
# Input second score, casting the string result to integer.
tScore2 = int(input("Please enter your second test score(0 to 100)"))

# Calculate the average: sum scores, divide by 2, and round the float result to 1 decimal place.
average = round(float((tScore1 + tScore2) / 2), 1)

# Format the output message and create a dynamic border based on its length.
msg = f"average score is {average}"
border = "-" * len(msg)

# Print the final result block.
print(border)
print(msg)
print(border)

# Farewell message, reusing the initially captured string input.
print("Thanks,", user_name)

end user_input_demo.py
