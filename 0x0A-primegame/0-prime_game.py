#!/usr/bin/python3
"""
Prime Game - Maria and Ben
"""


def is_prime(n):
    """
    Checks if the number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Checks if the number is a winner
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(2, n+1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# # Example usage:
# nums = [4, 5, 1]
# print(isWinner(nums))  # Output: Ben
