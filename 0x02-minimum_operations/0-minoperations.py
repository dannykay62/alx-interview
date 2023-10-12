#!/usr/bin/env python3
"""
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste.
    Given a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
"""
def minoperations(n):
    if n == 1:
        return 0
    
    # Initialize an array to store the minmum number of operations for each number
    dp = [0] + [float('inf')] * n

    for i in range(2, n + 1):
        # If i is prime, it takes i number of operations to reach H characters
        if n % i == 0:
            dp[i] = i
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    # If i is not, calculate the minimum operations according to its factors
                    dp[i] = min(dp[i], dp[j] + dp[i // j])

    return dp[n]
