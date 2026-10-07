# Functions, Tuples, Dictionaries, and Exceptions

## Overview

This lab helped me practice Python functions, tuples, dictionaries, and exception handling.

## Files

### basic_functions.py
- Created functions with parameters and return values.
- Used `greet_user()`, `add_two_numbers()`, and `is_even()`.

### calc_with_functions.py
- Created separate functions for addition, subtraction, multiplication, and division.
- Used one function to call other functions.
- Used `try/except` to handle invalid numbers and division by zero.

### tuples_dicts.py
- Created a tuple containing the twelve months.
- Accessed tuple values using indexes.
- Learned that tuples are immutable.
- Created and updated a dictionary of students and grades.
- Used `.items()` to loop through dictionary keys and values.

### data_processing.py
- Created a dictionary containing courses and tuples of grades.
- Created a function to calculate the average grade.
- Used `try/except` to handle an empty tuple.

### exception_demo.py
- Used `raise` to create a `ValueError`.
- Used `except` to catch exceptions.
- Used `finally` to run code whether an exception occurred or not.
- Used a generic `Exception` to catch an invalid string-to-integer conversion.

## Sample Output

```text
Result: 5.0
Division operation completed
Error: Cannot divide by zero
Division operation completed
Generic error: invalid literal for int() with base 10: 'hello'