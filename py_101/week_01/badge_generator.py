# badge_generator.py
# Simple Python user badge generator with custom border
# Author: Michael Chipman
# Date: 2025-11-04
#
# TECHNICAL CONCEPTS DEMONSTRATED:
# - Variable Assignment (int and str types)
# - Type Checking (type() function)
# - Error Handling (TypeError demo and fix)
# - Error Handling (NameError demo and fix)
# - String Creation (single/double quotes, escaping as needed)
# - String Manipulation (concatenation '+', repetition '*' operators)
# - f-String Formatting (for readable output)
# - Built-in Function (len() for aligning borders)
# - Clear, professional code commenting
#
# Demonstrates all foundational variable, string, and error concepts in one file.

# store a name for the badge to display
name = "Tommy Price"

# store the age of the person on the badge as a string
age = "30"

# display value types stored in the variables
print(f"name is type: {type(name)} and age is type: {type(age)}")

# Demonstrate (and fix) a TypeError
# print(age + 5)    # This would fail: can't add str and int
print(int(age) + 5)

# Demonstrate (and fix) a NameError
# print(job_title)  # This would fail: can't use undeclared variable
job_title = "AI Engineer"
print(job_title)

msg = f"{name} | Age: {age}"

# print top border of badge
print(f'#' * len(msg))

# printing string output: Tommy Price | Age: 30 using f-string
print(msg)

# adding job title to badge
print(job_title)
# print bottom border of badge
print(f"#" * len(msg))

# end of badge_generator.py
