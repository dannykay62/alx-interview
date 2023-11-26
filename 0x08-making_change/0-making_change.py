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
    # sort the coins array
    coins.sort()

    dp_arr = [float('inf')] * (total + 1)
    dp_arr[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp_arr[i] = min(dp_arr[i], dp_arr[i - coin] + 1)

    return dp_arr[total] if dp_arr[total] != float('inf') else -1
