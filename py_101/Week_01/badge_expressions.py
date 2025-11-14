# badge_expressions.py
# Advanced Python price board with dynamic emoji border and detailed info
# Author: Michael Chipman
# Date: 2025-11-04
#
# TECHNICAL CONCEPTS DEMONSTRATED:
# - Variable Assignment (int, float, str)
# - String Concatenation and Repetition ('+', '*' operators)
# - f-String Formatting with math expressions and :.2f
# - len() for dynamic border sizing
# - Operator Precedence (+, -, *, /)
# - Parentheses to control evaluation order
# - type() function for type checking

# store two food items and thier prices
food = "Bison Burger"
food_price = 20
drink = "Root Beer"
drink_price = 4

# Store sales_tax and custom special_fee
sales_tax = 0.07
special_fee = 0.09

# combine food item names and repeat them 3 times then print them.
combine_names = (food + drink) * 3
print(combine_names)

# check the types of the data stored to ensure proper math
print(f"{food} is of type {type(food)} and food_price: {food_price} is of type {type(food_price)}")
print(f"{drink} is of type {type(drink)} and drink_price: {drink_price} is of type {type(drink_price)}")

# store the total of both products including sales_tax and special_fee
total = (food_price + drink_price) * (1 + sales_tax + special_fee)

# store message for output
msg = f"One {food} and one {drink} after special fee and sales tax is ${total:.2f}"

#print the message
print(msg)

# end of badge_expressions.py
