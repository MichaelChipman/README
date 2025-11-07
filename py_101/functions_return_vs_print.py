"""
functions_return_vs_print.py
Lesson 12 – Functions III: print vs return & early return
Purpose: Compare print and return in functions, practice passing values, dynamic formatting, and early return.
Author: Michael Chipman
Date: 2025-11-07

Technical concepts demonstrated:
- Difference between print() and return in functions
- Storing and formatting returned values with f-strings
- Dynamic string borders using len()
- Early return: exiting a function before the end
- Writing simple markup and discount functions
- Debug output and return value handling
"""

def greet():
    """
    Returns a standard greeting message.

    Returns:
        str: The fixed greeting string.
    """
    return "Hello from inside the function!"

# Execute the function and capture its return value
message = greet()
# Print the value returned by the function
print(message)
# Print a message from the global scope
print("Hello from outside the function!")

# -------- New Function total() ---------

def total():
    """
    Provides a fixed numerical value representing a total.

    Returns:
        float: A constant monetary value (19.975).
    """
    return 19.975

# Call the function and assign the float result
result = total()
# Format the result as currency with two decimal places using an f-string
decorated = f"The total is: ${result:.2f}"
# Create a separator line matching the length of the formatted string
border = "-" * len(decorated)
# Display the formatted total bordered by the separator lines
print(border)
print(decorated)
print(border)

# --------- New Function debug_and_quit() ----------

# This function demonstrates the effect of an unconditional early return
def debug_and_quit():
    '''
    Illustrates immediate function exit using 'return'.

    Prints "start" but exits before "end" is reached, demonstrating
    how code after an unconditional return is unreachable.

    Args:
        None: Takes no arguments.

    Returns:
        None: The function returns implicitly or explicitly without a value.
    '''
    print("start") # This line executes successfully
    return # The function exits here
    print("end") # This line is unreachable and never executes

# Demonstration: calls debug_and_quit() to show the early exit
debug_and_quit()

# --------- New Function area_rect() --------------
# Demonstrates using an early return as a debugging breakpoint
def area_rect(width, height):
    """
    Calculates the area of a rectangle.

    NOTE: This function contains an unconditional early return for debugging
    purposes, preventing the area calculation from ever being reached.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        None: Due to the unconditional early exit.
    """
    print("DEBUG: width:", width) # Debug message prints parameter value
    return # Halts execution immediately; no area calculated
    # The following line is unreachable code
    area = width * height

# Call the function for side effects (printing debug message)
area_rect(25, 5)
# Call the function again and store the resulting None value
result = area_rect(25, 5)
# Print the result (which is None)
print(result)

# --------- New Function markup() --------------

def markup(price, pct):
    """
    Calculates the new price after applying a percentage increase.

    Args:
        price (float): The original base price.
        pct (float): The percentage increase (e.g., 0.08 for 8%).

    Returns:
        float: The final price including the markup.
    """
    price_increase = price * (1 + pct)
    return price_increase

# Calculate and store the marked-up price
increased_price = markup (100, 0.08)
# Print the calculated price
print(increased_price)

# --------- New Function discount() --------------

def discount(price, pct):
    """
    Calculates the new price after applying a percentage decrease.

    Args:
        price (float): The original base price.
        pct (float): The percentage decrease (e.g., 0.08 for 8%).

    Returns:
        float: The final price after the discount.
    """
    price_decrease = price * (1 - pct)
    return price_decrease

# Calculate and store the discounted price
reduced_price =  discount(100, 0.08)
# Print the calculated price
print(reduced_price)

# end functions_return_vs_print.py
