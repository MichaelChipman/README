"""
elif_order_dependence.py
Lesson 22: Elif Order Dependence and Short-Circuiting
Purpose: Demonstrates how the order of conditions in an elif ladder critically determines 
         the logic path and final result due to short-circuiting.
Author: Michael Chipman
Date: 2025-11-12

Technical Concepts Demonstrated:
- If/Elif Short-Circuiting (Execution halts on the first True condition)
- Order Dependence in Conditional Logic
- Defining and Using Boolean Flags
- In-line Single-Statement Conditionals (Concise syntax)
- Input and Type Casting with float()
- String Formatting (f-string with :.2f for currency)
"""

# ----------- Defining Boolean Flags -----------
# Initialize a numeric variable.
age = 15
# Define a boolean flag based on a condition (False, since 15 is not < 13).
is_child = age < 13
# Define a second boolean flag (True, since 15 is < 18).
is_teen = age < 18

print(is_child)
# Check the first flag. If True, the block executes and skips the rest.
if is_child:
    print("child")
# Check the second flag. Executed only if the 'if' condition was False.
elif is_teen:
    print("teen")
# Executed only if both preceding conditions were False.
else:
    print('adult')

# ----------- Order Dependence: Incorrect Logic -----------
# Reset the value.
age = 18
# Incorrect Order: The "young" condition (age < 18) should come *after* "kid" (age < 13) 
# because 18 is not < 18. This prints "adult".
if age < 18: 
    print("young")
# This condition is never reached because the primary condition was False and elifs are sequential.
elif age < 13: 
    print("kid")
# This is the only block reached when age is 18.
else: 
    print("adult")

# ----------- Order Dependence: Correct Logic -----------
# Reset the value.
age = 18
# Correct Order: The smaller, more specific range (age < 13) is checked first.
if age < 13: 
    print("kid")
# The broader range (age < 18) is checked second. Since age is 18, this is False.
elif age < 18: 
    print("young")
# This block executes for age 18, which is the correct categorization.
else: 
    print("adult")

# ----------- Ordered Pricing Logic (Short-Circuiting) -----------
# Prompts the user and explicitly casts the input string to a float for comparison.
weight = float(input("What is the weight?"))

# Check the smallest, most specific bucket first (weight <= 1).
if weight <= 1:
    cost = 5
    # Prints cost formatted to two decimal places (currency).
    print(f"${cost:.2f}")
# Check the next range (weight <= 5). This is only reached if weight is > 1.
elif weight <= 5:
    cost = 10
    print(f"${cost:.2f}")
# Check the next range (weight <= 20). This is only reached if weight is > 5.
elif weight <= 20:
    cost = 20
    print(f"${cost:.2f}")
# The catch-all for anything over 20.
else:
    print("too heavy")
    
# end elif_order_dependence.py
