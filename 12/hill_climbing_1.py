"""
Credit to William Y. Feng for his video on this problem, linked below, for
inspiration on implementing Dijkstra's algorithm.
https://youtu.be/sBe_7Mzb47Y
"""

import numpy as np
import sys
from heapq import heappop, heappush


def parse(input_text: str) -> tuple[list[list[int]],
                                    tuple[int, int],
                                    tuple[int]]:
    """
    Parses the input text of an elevation map where each lowercase letter from
    a to z represents a height from 0 to 25, and S and E represent start and
    ending locations.

    Args:
        input_text: A string representing a 2-D grid of letters.

    Returns:
        A tuple of: (1) a numpy 2-D arrayof integers representing the heights
        of the 2-D grid; (2) a tuple representing the starting index; (3) a
        tuple representing the ending index.
    """
    grid = [list(row) for row in input_text.split('\n')]
    grid = [x for x in grid if len(x) > 0]

    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter == 'S':
                start = (r, c)
                grid[r][c] = 0
            elif letter == 'E':
                end = (r, c)
                grid[r][c] = 25
            else:
                grid[r][c] = ord(letter) - ord('a')
    return (np.array(grid), start, end)


def neighbors(grid: list[list[int]], pos: tuple[int, int]) -> tuple[int, int]:
    """
    A generator function that returns valid neighbors for a certain position in
    the grid.

    Args:
        grid: A numpy 2-D array of integers.
        pos: The position to check.

    Returns:
        A generator that returns valid neighbors where the height is no more
        than one level above the current position. The generator always returns
        neighbors in the order of north, east, south, and west.
    """
    height, width = grid.shape
    for delta_r, delta_c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_r = pos[0] + delta_r
        new_c = pos[1] + delta_c

        if not (0 <= new_r < height and 0 <= new_c < width):
            continue

        if grid[new_r, new_c] <= grid[pos] + 1:
            yield (new_r, new_c)


def dijkstra(grid: list[list[int]],
             start: tuple[int, int],
             end: tuple[int, int]) -> int:
    """
    An implementation of Dijkstra's algorithm for pathfinding.

    Args:
        grid: A 2-D numpy array of integers representing heights, where a path
        from one location to another can go up at most one unit of height.
        start: A tuple representing the starting location
        end: A tuple representing the ending location

    Returns:
        An integer representing the length of the shortest path from the start
        to the end.
    """
    visited = np.full(grid.shape, False)
    queue = [(0, start)]

    while True:
        steps, position = heappop(queue)
        if visited[position]:
            continue
        visited[position] = True

        if position == end:
            print(steps)
            break

        for neighbor in neighbors(grid, position):
            heappush(queue, (steps + 1, neighbor))


if __name__ == '__main__':
    dijkstra(*parse(sys.stdin.read()))
