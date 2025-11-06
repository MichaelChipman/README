"""
functions_return_practice.py
Lesson 11 – Functions II: inside the function
Purpose: Show function structure, tracing values, using and returning results from a function.
Author: Michael Chipman
Date: 2025-11-06

Technical concepts demonstrated:
- Function structure (definition, parameters, indentation)
- Return statements and receiving function output
- Side effects (debugging print statements)
- Formatting output (f-strings, round())
- Naming conventions (avoiding variable shadowing, type checking)
"""

# --- Function Definition and Signature: total() ---
# Defines the function 'total' with two required parameters: price and qty.
def total(price, qty): 
    # Calculation: Performs the primary arithmetic operation (price * qty).
    subtotal = price * qty 
    
    # Side Effects: Debug logging for input parameters and calculated subtotal.
    print("DEBUG price:", price) 
    print("DEBUG qty:", qty)
    print("DEBUG subtotal:", subtotal) 
    
    # Explicit Return: Returns the final calculated value, rounded to two decimal places.
    return round(subtotal, 2)

# --- Function Call and Final Output ---
# Executes the function with arguments (9.99, 3) and prints the returned value (29.97).
print(total(9.99, 3))

# --- Function Definition and Signature: area_rect() ---
# Defines the function 'area_rect' with two required parameters: width and height.
def area_rect(width, height):
    # Calculation: Performs the primary arithmetic operation (width * height).
    area = width * height # Avoided shadowing by not using a function name for the variable name.

    # Side Effects: Debug logging for input parameters and calculated area.
    print("DEBUG width:", width)
    print("DEBUG height:", height)
    print("DEBUG area:", area)
    
    # Explicit Return: Returns the final calculated value.
    return area

# Store returned value, formatting output using an f-string.
msg = f"area = {area_rect(4, 5)}"
# Creates dynamic border using len() to get the length of msg.
border = "-" * len(msg)
# Prints the message between two borders.
print(border, msg, border, sep="\n")

# --- Function Definition and Signature: discount() ---
def discount(price, pct):
    """
    Calculates and returns the price after applying the specified percentage discount.

    Args:
        price (float): The original price.
        pct (float): The discount percentage (e.g., 0.15 for 15%).
        
    Returns:
        float: The discounted price, rounded to two decimal places.
    """
    # Calculation: Performs the primary arithmetic operation to find the discounted price.
    discounted_price = price * (1 - pct)

    # Side Effects: Debug logging for parameter values, type of 'pct', and final calculated variable.
    print("DEBUG price value:", price)
    print("DEBUG pct value:", pct)
    print("DEBUG pct type:", type(pct))
    print("DEBUG discounted_price:", discounted_price)

    # Explicit Return: Returns the final calculated value rounded to 2 decimal spaces.
    return round(discounted_price, 2)
    
# Define variables for original price and discount percentage.
original_price = 24.99
discount_pct = 0.15

# Display the original price and the result returned by the discount function.
print(f"The original price is: $ {original_price}")
print(f"the price after the discount is: ${discount(original_price, discount_pct)}")

# end functions_return_practice.py
