'''
python_errors.py
Lesson 14 – Python errors: meet the traceback
Purpose: Show how to read the traceback for Debug
Author: Michael Chipman
Date: 2025-11-06

Technical concepts demonstrated:
- Reading Python tracebacks to find the error location, error type, and meaning.
- Identifying the file, line number, and code that caused the error.
- Recognizing common error types: NameError, TypeError, UnboundLocalError, 
  ZeroDivisionError.
- Always checking the last line of the traceback first for the error type and message.
- Using errors to debug, not as failure signs.
'''

'''
Shows NameError and traceback message
Traceback (most recent call last):
  File "main.py", line 2, in <module> # error location
    print(scor) # error location
NameError: name 'scor' is not defined. Did you mean: 'score'? # error type: message
The meaning was python tried to use variable scor but it wasn't defined anywhere above
'''
# ------------- NameError ------------

# score = 12
# print(scor)

# ------------ TypeError -------------

'''
shows TypeError
 Traceback (most recent call last):
 TypeError: can only concatenate str (not "int") to str
 - meaning python tried to add an integer to a string
 - the + operator attempts to use arithmetic 
 - operations on numbers and attempts to concatenate strings.
 - python can't combine a string with a number using + raising the TypeError
'''

# print(type("score: "))
# print(type(10))
# print("score: " + 10)

# ---------- UnboundLocalError ---------------

'''
Shows UnboundLocalError
Traceback (most recent call last):
UnboundLocalError: cannot access local variable -
-  'score' where it is not associated with a value
This occurs if you forget to add a parameter to the function with the same name,
 or you forget to instantiate the variable with a value before attempting to 
 use += or -= because python thinks it is a new local variable without a value
'''
score = 5

def bump():
    score += 1
    print(score)

bump()

# I always read the last line of a Python traceback first
# end python_errors.py
