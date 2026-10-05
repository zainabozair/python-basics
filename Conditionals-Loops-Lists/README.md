# Conditionals, Loops, and Lists

This assignment covers Python conditional statements, loops, list operations, logical operators, bitwise operators, and bubble sort.

## 1. Grade Checker

The grade checker takes a numeric grade from 0–100 and uses `if`, `elif`, and `else` statements to determine the letter grade. It also uses a conditional expression to display a final message.

### Example Output

```text
Please enter numeric grade 0-100: 85
Your grade is: B
Congratulations!
```

## 2. Even Sum

This program calculates the sum of even numbers from 1 to 50 using both a `for` loop and a `while` loop.

### Output

```text
The sum of even numbers from 1 to 50 is 650
The sum of even numbers from 1 to 50 in while is 650
```

Both loops give the same result. I find the `for` loop clearer because it is shorter.

## 3. List Operations

This program creates a list of integers and demonstrates different list operations, including `sorted()`, `.sort()`, `.append()`, removing an element, and `.reverse()`.

### Example Output

```text
Enter a number: 5
Enter a number: 8
Enter a number: 2
Enter a number: 10
Enter a number: 3
Original list: [5, 8, 2, 10, 3]
Sorted list: [2, 3, 5, 8, 10]
Sorted list: [2, 3, 5, 8, 10]
After append: [2, 3, 5, 8, 10, 30]
After removing an element: [3, 5, 8, 10, 30]
Reversed list: [30, 10, 8, 5, 3]
```

## 4. Bubble Sort

This program uses nested loops to perform a bubble sort. Neighboring elements are compared and swapped when they are in the wrong order.

The list after each complete pass is printed to show the sorting progress.

### Output

```text
Original list: [64, 25, 12, 22, 11]
Pass 1 : [25, 12, 22, 11, 64]
Pass 2 : [12, 22, 11, 25, 64]
Pass 3 : [12, 11, 22, 25, 64]
Pass 4 : [11, 12, 22, 25, 64]
Pass 5 : [11, 12, 22, 25, 64]
Sorted list: [11, 12, 22, 25, 64]
```

## 5. Logic and Bitwise Operations

This program demonstrates the logical operators `and`, `or`, and `not`. It also demonstrates bitwise operators using the integers 5 and 3 and displays the results in binary using `bin()`.

### Example Output

```text
Enter 1 for True or 0 for False: 0
Enter 1 for True or 0 for False: 1
a AND b: False
a OR b: True
NOT a: True
5 & 3: 0b1
5 | 3: 0b111
5 ^ 3: 0b110
~5: -0b110
5 << 1: 0b1010
5 >> 1: 0b10
```

## Files

- `Grade-Checker/grade_checker.py`
- `Even-Sum/even_sum.py`
- `Lists/list_operations.py`
- `Lists/bubble_sort_demo.py`
- `Logic-Bits/logic_bits.py`