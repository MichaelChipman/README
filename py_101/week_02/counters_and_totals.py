"""
counters_and_totals.py
Lesson 26: Data Aggregation with Counters and Totals
Purpose: Demonstrates real-world data collection and analysis by implementing counters (to track items) and totals (to sum values)
         using different loop types and robust 'try/except' exception handling.
Author: Michael Chipman
Date: 2025-11-13

Technical Concepts Demonstrated:
- Loop Initialization (Counter and Total Variables)
- For Loop (List Iteration)
- While True Loop (Infinite Loop)
- Break/Continue Statements (Control Flow)
- Try/Except (Exception Handling for Input Validation)
- Nested For Loop (Character iteration)
- Modulo Operator (Count checkpoint logic)
- Data Aggregation (Total and Average calculation)
"""
# --- Example 1: Basic For Loop Aggregation (Known List) ---
items = 0
total = 0

prices = [2.5, 4, 1.5]
for item in prices:
    items += 1
    total += item
print(items, total)

# -------------------------------------------------------------
# --- Example 2: Robust While Loop Aggregation (User Input) ---
num_scores = 0 
total = 0      

while True: # Infinite loop, relies on 'break' for termination
    try:
        score = input("Input a test score, type 'stop' when finished.")
        
        if score == "stop":
            break # Exit loop upon sentinel value
        elif score == "":
            continue # Skip iteration if input is empty
        else:
            num_scores += 1
            total += float(score) # Protected by 'try' block
            
    except: # Catches non-numeric input that fails the float() cast
        print("Invalid input, please enter a number or type 'stop'")
        continue # Skips bad input and asks again

# Final calculation logic: check for division by zero
if num_scores == 0:
    print("no scores entered")
else:
    print("Total Scores:", num_scores, "Average:", total / num_scores) 

# -------------------------------------------------------------
# --- Example 3: Nested Loops and Modulo Counter ---
vowels = 0
words = 0

while True:
    word = input("Enter a word, when done type 'stop'")
    
    if word == "stop":
        break
    elif word == "":    
        continue
    else:
        # Inner loop: Iterates over every character in the word
        for ch in word:
            if ch in "aeiouAEIOU":
                vowels += 1
        
    words += 1 
    # Modulo Logic: Print a checkpoint every 3 words
    if words % 3 == 0:
        print("--- Checkpoint: Total vowels counted so far:", vowels)

print("Vowels:", vowels)
print("Words:", words)

# end counters_and_totals.py
