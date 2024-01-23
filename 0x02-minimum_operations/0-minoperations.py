#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result in exactly
n H characters in the file
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            # Perform 'Copy All' operation for each prime factor
            n //= divisor
            operations += divisor

        divisor += 1

    return operations
