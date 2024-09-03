#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementa n en cada iteración
    return result

f = factorial(number)
print(f"{f}")