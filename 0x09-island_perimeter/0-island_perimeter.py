#!/usr/bin/python3

def island_perimeter(grid):
    per = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Check if the cell represents land
                # Check the top boundary
                if i == 0 or grid[i-1][j] == 0:
                    per += 1

                # Check the bottom boundary
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    per += 1

                # Check the left boundary
                if j == 0 or grid[i][j-1] == 0:
                    per += 1

                # Check the right boundary
                if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                    per += 1

    return per
