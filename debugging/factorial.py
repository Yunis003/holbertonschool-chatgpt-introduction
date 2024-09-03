#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to eventually end the loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Number must be non-negative.")
        f = factorial(number)
        print(f)
    except ValueError as e:
        print(e)
        sys.exit(1)

