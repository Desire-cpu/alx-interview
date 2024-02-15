#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = [False] * len(sieve[p*p:n+1:p])
    return [i for i in range(n + 1) if sieve[i]]


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0
    max_limit = max(nums)
    all_primes = primes(max_limit)

    for i in range(x):
        if all_primes.count(nums[i]) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
