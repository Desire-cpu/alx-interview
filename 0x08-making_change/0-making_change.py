#!/usr/bin/python3


"""
Making Change
"""


def minimum_coins_needed(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    # Check if the total is non-positive
    if total <= 0:
        return 0

    # Check if the coins list is empty or None
    if not coins:
        return -1

    try:
        # Check if the total can be directly satisfied by one coin
        coin_index = coins.index(total)
        return 1
    except ValueError:
        pass

    # Sort coins in descending order to optimize the greedy approach
    coins.sort(reverse=True)

    # Initialize the count of coins needed
    coin_count = 0

    # Iterate through the sorted coins
    for coin_value in coins:
        # Check if the total is a multiple of the current coin value
        if total % coin_value == 0:
            coin_count += int(total / coin_value)
            return coin_count

        # Check if the current coin value can be used to reduce the total
        if total - coin_value >= 0:
            # Check if multiple coins of the same value can be used
            if int(total / coin_value) > 1:
                coin_count += int(total / coin_value)
                total = total % coin_value
            else:
                coin_count += 1
                total -= coin_value
                if total == 0:
                    break

    # Check if the total amount could not be reached
    if total > 0:
        return -1

    return coin_count
