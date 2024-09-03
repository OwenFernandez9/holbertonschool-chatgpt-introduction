#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementa n en cada iteración
    return result

if len(sys.argv) != 2:
    print("Uso: python script.py <número>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("El número debe ser no negativo")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

f = factorial(number)
print(f)