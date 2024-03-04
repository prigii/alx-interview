#!/usr/bin/python3
"""
determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins
    # needed for each total from 0 to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    # Iterate through all possible totals from 1 to 'total'
    for t in range(1, total + 1):
        # For each coin value, check if it can contribute to the current total
        for coin in coins:
            if t - coin >= 0:
                # Update the minimum number of coins needed
                # for the current total
                dp[t] = min(dp[t], dp[t - coin] + 1)

    # If 'total' cannot be reached, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
