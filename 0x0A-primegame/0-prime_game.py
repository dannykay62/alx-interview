#!/usr/bin/python3
"""Prime game program"""


def is_prime(num):
    """Checks if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, numbers):
    """Counts total prime numbers in a given game"""
    def count_primes(num):
        """Counts total prime numbers in a given game"""
        count = 0
        for i in range(2, num + 1):
            if is_prime(i):
                count += 1
        return count

    def game_winner(num):
        """determine the game winner"""
        primes = count_primes(num)
        return "Maria" if primes % 2 == 0 else "Ben"

    winners = [game_winner(n) for n in numbers]

    maria_wins = winners.count("maria")
    ben_wins = winners.count("ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return "Ben"
