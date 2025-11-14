"""
scope_demo.py
Lesson 13 – Scope & Local Variables
Purpose: Illustrates the concept of variable scope, focusing on local and global variables in Python.
Author: Michael Chipman
Date: 2025-11-07

Technical concepts demonstrated:
- Global vs. local variable scope and lifespan.
- Variable shadowing (local variable hiding a global one of the same name).
- Using function parameters to provide necessary data and avoid reliance on globals.
- Function return values updating global state.
"""

meal = "burger"          # Global variable definition

def show_meal():
    """
    Demonstrates local scope and variable shadowing.

    A new local variable named 'meal' is created inside this function, 
    which temporarily hides the global 'meal' variable.

    Args:
        None

    Returns:
        None: Prints the local variable's value and type.
    """
    meal = "pizza"       # Local variable shadows the global one
    print("inside:", meal, "| type:", type(meal))
    # The local variable 'meal' is destroyed when the function finishes

# Call the function to demonstrate the local scope
show_meal()
# Reassign the global variable
meal = "salad"
# Print the global variable's current value
print("outside:", meal, "| type:", type(meal))

# ---------- New Function loud_border()---------------
def loud_border(text):
    """
    Decorates a given text string with a matching border above and below.

    The input text is converted to uppercase before printing.

    Args:
        text (str): The message string to be decorated.

    Returns:
        None: Prints the formatted output directly to the console.
    """
    # Create a border string using the length of the input text
    border = "-" * len(text)
    print(border)
    # Print the type of the locally created 'border' variable
    print(type(border))
    # Print the input text in uppercase
    print(text.upper())
    print(border)

# Demonstrate the loud_border function
loud_border("hello")
loud_border("pizza time")

# ---------- New Function markup()---------------
def markup(price, pct):
    '''
    Calculates the final price after applying a percentage markup.

    Args:
        price (float): The base price of the item.
        pct (float): The percentage increase (e.g., 0.15 for 15%).

    Returns:
        float: The final price after the markup has been applied.
    '''
    # Calculate the marked-up price
    price_markup = price * (1 + pct)
    return price_markup

# Call the markup function and print the result rounded to two decimal places (currency format)
print(round(markup(25.99, 0.15), 2))

# ------------New Function bump() ------------
# Define a global counter variable
count = 1

def bump(count):
    '''
    Increments a passed-in numerical value by one.

    This function demonstrates local scope: the 'count' parameter becomes a local
    variable, preventing the function from directly modifying the global 'count'
    variable. The new value must be explicitly returned and reassigned globally.

    Args:
        count (int): The current count value.

    Returns:
        int: The incremented count value.
    '''
    # Creates a local copy of count, which is incremented
    count = count + 1
    return count

# Call the function, capturing the returned (incremented) value and reassigning it
# to the global 'count' variable to effectively update the state.
count = bump(count)
# Print the updated global count
print(count)

# end scope_demo.py
