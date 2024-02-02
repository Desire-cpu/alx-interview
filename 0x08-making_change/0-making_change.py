#!/usr/bin/python3
""" Generates change  """


def makeChange(coins, total):
    """ Generate changes needed to reach total
    """
    if total <= 0:
        return 0
    look = 0
    temporary = 0
    coins.sort(reverse=True)
    for i in coins:
        while look < total:
            look += i
            temporary += 1
        if look == total:
            return temporary
        look -= i
        temporary -= 1
    return -1
