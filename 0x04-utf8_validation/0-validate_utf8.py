#!/usr/bin/python3

"""
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): List of integers representing the bytes of the .
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
"""


def validUTF8(data):

    """
    Check if data os a valid UTF-8 encoding

    Args:
        data: A list of bytes.

    Returns:
        True if data is a valid UTF-8 encoding, False otherwise.
    """

    for b in data:
        if b >> 7 == 0:
            continue
        elif b >> 5 == 0b110:
            continue
        elif b >> 4 == 0b1110:
            continue
        elif b >> 3 == 0b11110:
            continue
        else:
            return False
    return True
