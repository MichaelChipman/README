"""
elif_refactoring.py
Lesson 21: Elif and refactoring nested decisions
Purpose: Demonstrates the use of nested, compound, and chained conditional structures,
         along with practical application in validation and categorization logic.
Author: Michael Chipman
Date: 2025-11-10

Technical Concepts Demonstrated:
- Nested If/Else Statements (Branching within a branch)
- Compound Conditional Logic (Logical AND operator)
- Elif Ladder Structure (Ordered multi-way decision)
- Condition Order Dependence (Logic relies on checking the largest range first)
- Refactoring Deep Nested Conditionals
- Trade-off of If/Elif Exclusivity vs. Nested Complexity
"""

# ----------- Nested Conditionals -----------
# Initialize the value used for conditional checks.
x = 9
# Check the primary condition for the outer block.
if x > 5:
    # Check the secondary condition, executed only if the outer condition is True.
    if x < 20:
        print("A")
    # This block executes if x > 5 is True, but x < 20 is False.
    else:
        print("B")
# This final block executes only if the primary condition (x > 5) is False.
else:
    print("C")

# ----------- Compound Logic and Refactoring -----------
# Initialize the value used for conditional checks.
x = 9
# Refactored Logic: Flattens a deep, nested IF structure into a single, comprehensive check 
# using the 'and' operator for perfect match against three separate criteria (value, length, content).
if x > 5 and x < 20:
    print("A")
# This 'elif' condition is technically redundant in this structure,
# as it is only reached if x is 20 or greater.
elif x > 5:
    print("B")
# Executes only if both the 'if' and 'elif' conditions are false (i.e., x <= 5).
else:
    print("C")

# ----------- Complex Validation Logic -----------

# Original Nested Structure (Included for comparison of complexity and complete branch coverage):
# discount_code = "START20"
# if discount_code == "START20":
#     if len(discount_code) == 7:
#         if "20" in discount_code:
#             print("Valid code, 20% off!")
#         else:
#             print("Valid length, missing percent")
#     else:
#         print("Correct code, length error")
# else:
#     print("Unknown code")

# Initialize the string variable for validation checks (using the actual code from your lesson file).
discount_code = "SOMECOd24"
# Refactored Logic: This flat IF/ELIF structure is cleaner but creates a critical trade-off. 
# Because ELIF branches are mutually exclusive, the order is now critical, and not all original 
# failure paths may be guaranteed to be hit (unlike the original nested version).
if discount_code == "START20" and len(discount_code) == 7 and "20" in discount_code:
    print("Valid code, 20% off!")
# Check the first failure condition: missing the required substring "20".
elif "20" not in discount_code:
    print("Valid length, missing percent")
# Check the second failure condition: incorrect length.
elif len(discount_code) != 7:
    print("Correct code, length error")
# Executes if none of the specific validation checks passed.
else:
    print("Unknown code")

# ----------- Elif Ladder and Order Dependence -----------
# Initialize the value to be categorized.
price = 75
# Check the largest price range first. If True, subsequent checks are skipped.
if price > 100:
    print("big buck")
# Check the next range. This block is only reached if the price is NOT > 100.
elif price > 50:
    print("medium buck")
# Check the smallest range. This block is only reached if the price is NOT > 50.
elif price > 30:
    print("small fry")

# end elif_refactoring.py
