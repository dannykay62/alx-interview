#!/usr/bin/python3
""" determine the fewest number of coins needed to meet a given amount total
    Given a pile of coins of different values"""

def makeChange(coins, total):
    """
    Using the technique "Coin Change" or "Minimum Coin Change" algorithm
    determine the fewest number of coins needed to meet a given amount total
    Args:
        coins: int - is a list of the values of the coins in your possession
        total: int - amount to meet

    Return:
        fewest number of coins needed to meet total
    """
    if total < 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
