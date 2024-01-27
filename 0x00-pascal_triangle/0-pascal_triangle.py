#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integer, if n <= 0
    return an empty list.
    """
    lists = []
    if n <= 0:
        return lists
    lists = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(lists[i - 1]) - 1):
            curr = lists[i - 1]
            temp.append(lists[i - 1][j] + lists[i - 1][j + 1])
        temp.append(1)
        lists.append(temp)
    return lists
