'''
debugging_intro.py
Lesson 15 – introduction to debugging
Purpose: How to find and fix mistakes (“debugging”) using print() probes.
Author: Michael Chipman
Date: 2025-11-08

Technical concepts demonstrated:
- What “debugging” means in practice.
- Adding print() probes to trace variable values.
- Reading the console output to spot mistakes.
- Removing probes after fixing the bug.
'''
# ------------ debugging activity -----------
'''
Debugging steps taken
    1. created debug lines for tax_rate and tip_rate and tested them.
    2. created debug line for price and tested it.
    3. checked formula and corrected errors.
    4. deleted debug lines. 
'''
# price      = 12.99
# tax_rate   = 0.07
# tip_rate   = 0.15

# total_due = price * (1 + tax_rate + tip_rate)    # BUG: should multiply
# print("total due is", total_due)

# ---------- Function debugging practice ------------

def add_five(x):
    '''
    Debugging steps taken
        1. created debug line for x.
        2. corrected "5" changing it to int 
        3. ran program to verify error removed
        4. deleted debug line
    '''
 
    return x + 5    # BUG: mixing types

result = add_five(10)
print("Result is", result)

# When in doubt, add prints — then delete them when fixed.
# end debugging_intro.py
