#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Function Description:
    This function computes the factorial of a given non-negative integer `n` using recursion. 
    The factorial of a number `n` is the product of all positive integers less than or equal to `n`.

    Parameters:
    n (int): A non-negative integer for which the factorial needs to be calculated.

    Returns:
    int: The factorial of the input number `n`. Returns 1 if `n` is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Convert the first command-line argument to an integer
number = int(sys.argv[1])

# Calculate the factorial of the provided number
f = factorial(number)

# Print the result
print(f"{f}")