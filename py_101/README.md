# 🐍 Py 101: Foundational Python Scripts

This module documents foundational Python assignments covering core programming concepts, from basic syntax and data types to functions and control flow structures.

## Table of Contents

| Item | Status | Link |
| :--- | :--- | :--- |
| *[Back to Main Repository README.md](../README.md)* | | |
| *[Jump to Week 1 Lessons](#week-1-lessons)* | | |
| *[Jump to Week 2 Lessons](#week-2-lessons)* | | |
| *[Jump to Week 3 Lessons](#week-3-lessons)* | | |

---

## Week 1 Lessons

<details>
<summary>This foundational week covered core Python syntax, arithmetic operations, type casting, and the introduction of functional programming principles. **(Click to Expand 17 Lessons)**</summary>

| File | Status | Description |
| :--- | :--- | :--- |
| [`scoreboard.py`](scoreboard.py) | Complete (Lesson 1) | Demonstrates core Python syntax, variable management, user input/output handling, and effective in-line commenting. |
| [`badge_generator.py`](badge_generator.py) | Complete (Lesson 2) | Focuses on **Error Handling (TypeError/NameError)**, **Type Checking**, variable type conversion (`int()`), and advanced string creation for output. |
| [`badge_expressions.py`](badge_expressions.py) | Complete (Lesson 3) | Focuses on **Arithmetic Expressions**, **Operator Precedence**, `f-string` formatting with math (`:.2f`), and type handling (int, float) for accurate calculations. ([Title: [Py 101 - Lesson 3] Price Board Project: Mastering Arithmetic & Operator Precedence**](https://www.reddit.com/r/maestro/comments/1oo1a3s/title_py_101_lesson_3_price_board_project/)) |
| [`badge_update_print.py`](badge_update_print.py) | Complete (Lesson 4) | Focuses on **Compound Assignment** (`+=`, `-=`), variable reassignment, **comma-separated `print()`**, and the use of the **`round()`** function to correct **floating-point imprecision** due to the base-2 system. |
| [`balance_board.py`](balance_board.py) | Complete (L4 Stretch) | A dedicated stretch challenge project demonstrating **tuple creation** via comma assignment, the resulting `len()` constraint, and the required **string concatenation workaround** for calculating dynamic border sizes. |
| [`modeling_real_world_calculations.py`](modeling_real_world_calculations.py) | Complete (Lesson 5) | Focuses on translating word problems, comparing expression clarity, and a deep dive into **Type Errors** and **String/Tuple data type constraints** when using concatenation (`+`) versus explicit `str()` casting. |
| [`division_ops.py`](division_ops.py) | Complete (Lesson 6) | Focuses on the three division operators: **True Division (`/`)**, **Floor Division (`//`)**, and the **Modulo Operator (`%`)** for finding quotients and remainders in practical, real-world applications (e.g., time and boxes). |
| [`modulo_practice.py`](modulo_practice.py) | Complete (Lesson 7) | Focuses on advanced applications of the **Modulo Operator (`%`)** for determining **parity** (even/odd), calculating **cycle repetition**, and finding a specific **position** within a repeating sequence (e.g., scheduling). |
| [`rounding_and_money.py`](rounding_and_money.py) | Complete (Lesson 8) | Demonstrates **currency formatting** by distinguishing between **value rounding** (`round()`) and **output formatting** (`:.2f`), explicitly addressing floating-point imprecision and reusing the Modulo Operator for scheduling. |
| [`user_input_demo.py`](user_input_demo.py) | Complete (Lesson 9) | Focuses on **user input (`input()`)** and **explicit type casting** (`int()`, `float()`), demonstrating how to handle raw string input and convert it into numerical data required for calculations like averaging test scores. |
| [`functions_i.py`](functions_i.py) | Complete (Lesson 10) | Introduces **functional programming**, demonstrating the core concepts of **definition (`def`)**, **calling**, and using **parameters (arguments)** to create reusable, organized, and self-documenting code with `docstrings`. |
| [`functions_return_practice.py`](functions_return_practice.py) | Complete (Lesson 11) | Focuses on the **`return` statement**, demonstrating how functions pass data back to the calling scope. It explicitly contrasts function output (return value) with **side effects** (debugging `print` statements). |
| [`functions_return_vs_print.py`](functions_return_vs_print.py) | Complete (Lesson 12) | Compares the function of `print()` vs. `return`, demonstrates dynamic formatting, and illustrates the use of the early return statement. |
| [`scope_demo.py`](scope_demo.py) | Complete (Lesson 13) | Demonstrates global vs. local variable scope, variable shadowing, and how the return statement is necessary to update global state. |
| [`python_errors.py`](python_errors.py) | Complete (Lesson 14) | Demonstrates how to read and interpret Python tracebacks and identifies common errors like NameError, TypeError, and UnboundLocalError. |
| [`debugging_intro.py`](debugging_intro.py) | Complete (Lesson 15) | Introduces fundamental debugging practices, including using `print()` probes to trace variable values and identifying bugs in basic arithmetic and type-mixing operations. |
| [`mini_receipt_calculator.py`](mini_receipt_calculator.py) | Complete (Wk 1 Review) | A capstone project demonstrating **user input**, **explicit type casting**, **function definition**, and advanced **f-string currency formatting** to generate a real-store receipt layout. |

</details>

## Week 2 Lessons

<details>
<summary>This week covered decision structures, including `if/elif/else`, comparison and logical operators, and the critical distinction between identity and equality. **(Click to Expand 9 Lessons)**</summary>

| File | Status | Description |
| :--- | :--- | :--- |
| [`decisions_vs_repetitions.py`](decisions_vs_repetitions.py) | Complete (Lesson 16) | Introduces the foundational concepts of **decision structures** (`#S`) and **repetition structures** (`#R`) by differentiating between conditional actions and iterative tasks. |
| [`if_else_mental.py`](if_else_mental.py) | Complete (Lesson 17) | Demonstrates core `if`/`else` syntax, the importance of **indentation** and **comparison operators**, including checking for parity using the **Modulo Operator (`%`)**. |
| [`logical_operations_demo.py`](logical_operations_demo.py) | Complete (Lesson 18) | Demonstrates **logical operators (`and`, `or`, `not`)**, how **truth tables** function, and the efficiency concept of **short-circuit evaluation** in conditional statements. |
| [`identity_vs_equality.py`](identity_vs_equality.py) | Complete (Lesson 19) | Explores the difference between **Value Equality (`==`)** and **Object Identity (`is`)**, including concepts like **Boolean representation**, **integer caching**, and **floating-point imprecision**. |
| [`string_membership_and_conditionals.py`](string_membership_and_conditionals.py) | Complete (Lesson 20) | Demonstrates the usage of the **`in`** and **`not in`** string membership operators and fundamental **`if/elif/else`** conditional control flow, including case sensitivity. |
| [`elif_refactoring.py`](elif_refactoring.py) | Complete (Lesson 21) | Demonstrates the **refactoring of nested `if` statements** into the `if/elif` structure, highlighting the trade-off between **complexity** and **conditional exclusivity**. |
| [`elif_order_dependence.py`](elif_order_dependence.py) | Complete (Lesson 22) | Demonstrates **order dependence** in `if/elif` ladders, showing how Python's **short-circuiting** critically affects which condition is evaluated as True. |
| [`for_loops_and_range.py`](for_loops_and_range.py) | Complete (Lesson 23) | Demonstrates all forms of the **`range()`** function (1, 2, and 3 arguments), including forward, reverse, and accumulating sums within **`for` loops**. |
| [`while_loop_basics.py`](while_loop_basics.py) | Complete (Lesson 24) | Demonstrates the structure of the **`while` loop**, focusing on the crucial need for a control (update/sentinel) variable to prevent **infinite loops**. |
| [`break_continue_and_exceptions.py`](break_continue_and_exceptions.py) | New (Lesson 25) | Demonstrates the control flow of **`break`** and **`continue`**, showing how to build **robust input loops** using `while True` and basic **`try/except`** exception handling. |

</details>

## Week 3 Lessons

<details open>
<summary>This week introduces iteration fundamentals, covering the `for` and `while` loop syntax and structure, along with control flow modifiers and exception handling for robust input. **(Click to Collapse 1 Lesson)**</summary>

| File | Status | Description |
| :--- | :--- | :--- |

</details>

---

### 🔨 Finalizing the Restructure

This structure is robust, professional, and visually achieves the clean accordion look you wanted.

Since the files are now relative to the `py_101/README.md`, the rule for the **Annotation Gem**'s output for the README line is:

**New Rule:** The path in the `README.md` line item must be simplified to just the filename (e.g., `[filename.py](filename.py)`).

Do you approve this final structure and the accompanying change to the **Annotation Gem**'s pathing rule?
