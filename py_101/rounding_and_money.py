"""
rounding_and_money.py
Lesson 8 – Rounding & Money Formatting (round(), :.2f)
Purpose: Show how to control floating-point precision with round(), and format money output for clarity.
Author: Michael Chipman
Date: 2025-11-06

Technical concepts demonstrated:
- round(x, n): round to n decimal places (float value changes)
- Money display: f"{value:.2f}" (string representation only, 2 decimals for dollars/cents)
- Dynamic borders: "-" * len(string)
- Quick modulo reuse: n % cycles for fast position/cashier logic
- type(): inspect value vs representation
"""

print(round(5.6789, 2)) # round(x, n) returns a float rounded to 'n' decimal places.

print(0.1 + 0.2) # Demonstrates floating-point imprecision when stored in binary.
print(round(0.1 + 0.2, 2)) # Use round() to mitigate imprecision for calculation accuracy.

subtotal = 23.689999999999998
print(subtotal) # Display the raw, imprecise float value.
print(round(subtotal, 2)) # Apply round() to correct the float value to two decimal places.

rounded = round(subtotal, 2)
print(type(rounded)) # Confirms that round() returns a float data type.
print(f"${rounded:.2f}") # Use f-string formatting (:.2f) to display the float as a currency string.

print(f"{subtotal}  {rounded}   ${rounded:.2f}")
msg = f"${rounded:.2f}"
border = "$" * len(msg)
print(border)
print(msg)
print(border)

price = 12.49
qty = 3
tax_rate = 0.0875
# Calculate the raw total before rounding, exposing potential imprecision.
total_raw = price * qty * (1 + tax_rate)
# Round the calculated value to two decimal places for financial accuracy.
total_val = round(total_raw, 2)
msg = f"Total: ${total_val:.2f}"
border = "-" * len(msg)
print(border)
print(msg)
print(border)

order_number = 23 # order_number starts at 1 for this example
cashiers = 4 # rotating cashiers

# Modulo Operator used to cycle through 4 cashiers (results in 0, 1, 2, or 3).
print(f"Cashier {order_number % cashiers} is your server tonight")

# end rounding_and_money.py
