#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Function description:
	Computes the factorial of a non-negative integer using recursion.

	Parameters:
	n (int): A non-negative integer whose factorial is to be calculated.

	Returns:
	int: The factorial of the given integer n.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

# Convert the command-line argument to an integer
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
