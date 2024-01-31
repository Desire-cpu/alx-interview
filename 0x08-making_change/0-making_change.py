#!/usr/bin/python3


"""Change making module."""


def minimum_coins_needed(coins, target_amount):
    """
    Calculate the minimum number of coins needed to make up the target amount.

    Args:
    coins (list): List of coin denominations.
    target_amount (int): The target amount to make up with coins.

    Returns:
    int: Minimum number of coins needed, or -1 if it's not possible.
    """

    if target_amount <= 0:
        return 0

    # Create an array to store the minimum number of coins required t.
    min_coins = [float('inf')] * (target_amount + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, target_amount + 1):
            # Update the minimum number of coins required for each value
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins required to reach the target amount
    return min_coins[target_amount] if min_coins[target_amount] != float('inf') else -1
