#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """function def island_perimeter(grid): that returns the perimeter of
        the island described in grid:
        grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
        The grid is completely surrounded by water
        There is only one island (or nothing).
        The island does not have “lakes” (water inside that is not connected to the
        water surrounding the island)
    """
    perimeter = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]:
                if x == 0 or not grid[y][x - 1]:
                    perimeter += 1
                if x == len(grid[0]) - 1 or not grid[y][x + 1]:
                    perimeter += 1
                if y == 0 or not grid[y - 1][x]:
                    perimeter += 1
                if y == len(grid) - 1 or not grid[y + 1][x]:
                    perimeter += 1
    return perimeter
