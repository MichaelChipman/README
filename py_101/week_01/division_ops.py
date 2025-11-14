"""
division_ops.py
Lesson 6 – Division modes: / vs // with quotient and remainder
Purpose: Demonstrate quotient & remainder using practical examples (cookies, time).
Author: Michael Chipman
Date: 2025-11-05

Technical concepts demonstrated:
- True Division (/)
- Floor Division (//)
- Modulo Operator (%)
- Practical application of division for real-world problems.
"""
print(7 / 2) # True Division: Returns a floating-point result.
print(7 // 2) # Floor Division: Returns the integer quotient (drops decimals).

# Border calculation for true division output.
print("-" * len("True division: " + str(19 / 4) ))
print("true division:", 19 / 4) # Execute true division (/) operation.
# Border calculation for floor division output.
print("-" * len("floor division: " + str(19 // 4) ))
print("floor division:", 19 // 4) # Execute floor division (//) operation.

print(19 % 4) # Modulo Operator: Calculates the remainder of the division.

# --- Practical Application: Cookies ---
cookies = 23 # total number of cookies made
per_box = 5 # max number of cookies that fit in a box

# Floor Division: Finds the number of full boxes (the quotient).
full_boxes = cookies // per_box
# Modulo Operator: Finds the number of leftover cookies (the remainder).
leftover   = cookies %  per_box

# Create string representations for dynamic border calculation.
label_full_boxes = "Full boxes: " + str(full_boxes)
label_leftover = "leftover cookies: " + str(leftover)

# Print bordered output for full boxes.
print("-" * len(label_full_boxes))
print("Full boxes: " + str(full_boxes)) # Final output: Display the calculated number of full boxes.

# Print bordered output for leftovers.
print("-" * len(label_leftover))
print("leftover cookies: " + str(leftover))

# --- Practical Application: Time Conversion ---
total_seconds = 130 # Define the total time in seconds.
seconds_in_minute = 60 # Define the conversion factor (seconds per minute).

# Use // and % to find the minutes (quotient) and remaining seconds (remainder).
minutes = total_seconds // seconds_in_minute
seconds = total_seconds % seconds_in_minute
# Prepare the message string for border calculation.
message = str(minutes) + "min" + str(seconds) + "sec"
print("-" * len(message)) # Print the dynamic border for the time conversion output.
print(str(minutes) + " min " + str(seconds) + " sec") # Final output: Display the converted time in minutes and seconds.

# end division_ops.py
