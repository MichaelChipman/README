'''
functions_i.py
Lesson 10: Functions i: why, define, and call
purpose: Demonstrating the basic syntax for defining and calling Python functions.
Author: Michael Chipman
Date: 2025-11-06

Technical Concepts Demonstrated
- Function definition (def) and calling
- Function parameters (arguments)
- Using docstrings for clear documentation
- Function side effects (printing vs. returning)
'''

# --- Simple Functions: No Parameters, No Return ---

def border():  
    """Prints a horizontal border composed of 20 dashes."""
    print("-" * 20)

# Call the border 3 times for visual separation
border()
border()
border()

# --- Single Parameter Function ---

def greet(name):
    """Prints a simple 'Hello' greeting using the provided name."""
    print(f"Hello {name}")

greet("Michael")    # Test with a string constant (literal)

user_name = "Tom"
greet(user_name)    # Test with a variable

# user_name = input("Print your name") # Example: Use user input
# greet(user_name)

# --- Multi-Parameter Function (Prints Output) ---

def total(price, qty):
    """
    Calculates the subtotal (price * qty) and displays the result 
    in a formatted, bordered message. This function prints the output.
    """
    subtotal = price * qty
    msg = f"total due $ {round(subtotal, 2):.2f}"
    # Create a border that matches the length of the message
    border = "-" * len(msg) 
    print(border, msg, border, sep="\n")

total(7.95, 4)
total(12.80, 2)

# --- Function with a Detailed Docstring ---

def average(score1, score2):
    """
    Prints the average of two scores with a bordered message.
    
    Parameters:
        score1: The first number (score).
        score2: The second number (score).
    """
    average = (score1 + score2) / 2
    msg = f"your score average is {round(average, 1)}"
    border = "-" * len(msg)
    print(border, msg, border, sep="\n")

average(97, 82)

# end functions_i.py
