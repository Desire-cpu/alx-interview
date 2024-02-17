#!/usr/bin/python3
"""
N-Queens Problem Solver
"""

import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """
    Backtrack function to find solutions to the N-Queens problem
    """
    if row == n:
        solutions = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 1:
                    solutions.append([r, c])
        print(solutions)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solve the N-Queens problem and print all solutions
    Args:
        n (int): Number of queens. Must be >= 4
    Returns:
        List of lists representing coordinates of each queen.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n_value = int(args[1])
        if n_value < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n_value)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
