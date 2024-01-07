#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): List of integers representing the bytes of the UTF-8 encoding.
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
"""


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    """
    num = 0
    for byte in data:
        mask = 1 << 7
        if not num:
            while byte & mask:
                num += 1
                mask >>= 1
            if not num:
                continue
            if num == 1 or num > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num -= 1
    return num == 0
