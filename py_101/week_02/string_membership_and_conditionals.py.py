"""
string_membership_and_conditionals.py
Lesson 20: String Membership and Conditional Control Flow
Purpose: Demonstrates the use of the 'in' and 'not in' operators for string checking,
         and fundamental if/elif/else structures for conditional execution.
"""

# Check for basic substring membership using the 'in' operator. The result is a boolean (True/False).
print("lo" in "hello")
# ---------------
# Use 'in' within an if/else block to control program flow based on string content.
msg = "spam found"
if "spam" in msg:
    print(msg)
else:
    print("not found")
# --------------
# Check for basic substring non-membership using the 'not in' operator.
print("@" not in "hello")
# --------------
# Use 'in' for simple validation, checking if a required character is present.
user_id = "@admin"
if "@" in user_id:
    print("Welcome")
else:
    print("invalid id")
# ---------------
# Combine 'in' and 'not in' with logical operators ('and') for complex conditional rules.
# This checks if '@' is present AND 'admin' is NOT present.
if "@" in user_id and "admin" not in user_id:
    print("Welcome")
# ---------------
# Demonstration of case sensitivity in Python string membership checks.
# "he" is True, but "He" is False as Python is case-sensitive.
print("he" in "hello")
print("He" in "hello")
#---------------
# Full if/elif/else structure for multi-way decision making.
# Only the first block whose condition is True will execute.
choice = 'popcorn'
if choice == "quit":
    print("Exiting...")
elif choice == "menu":
    print("Opening menu...")
else:
    print("Unknown command")

# end string_membership_and_conditionals.py
