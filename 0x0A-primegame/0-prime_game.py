#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def primes(n):
    """
    Return list of prime numbers between 1 and n inclusive
    Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    # Sieve of Eratosthenes algorithm to find prime numbers
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if the winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0
    # Loop through each round
    for i in range(x):
        prime = primes(nums[i])
        # Count the number of primes in the current round
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    # Determine the winner based on the count of primes in all rounds
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'

    # Return None if no winner is found
    return None
