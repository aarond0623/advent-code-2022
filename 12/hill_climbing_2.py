import numpy as np
import sys
from heapq import heappop, heappush
from hill_climbing_1 import parse


def neighbors(grid: list[list[int]], pos: tuple[int, int]) -> tuple[int, int]:
    """
    A generator function that returns valid neighbors for a certain position in
    the grid. It is the opposite of the generator in part 1, and is meant for
    pathing in reverse.

    Args:
        grid: A numpy 2-D array of integers.
        pos: The position to check.

    Returns:
        A generator that returns valid neighbors where the height is no less
        than one level below the current position. The generator always returns
        neighbors in the order of north, east, south, and west.
    """
    height, width = grid.shape
    for delta_r, delta_c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_r = pos[0] + delta_r
        new_c = pos[1] + delta_c

        if not (0 <= new_r < height and 0 <= new_c < width):
            continue

        if grid[new_r, new_c] >= grid[pos] - 1:
            yield (new_r, new_c)


def dijkstra(grid: list[list[int]], start: tuple[int, int]) -> int:
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

        # Once we find a position with elevation 0, stop and print the steps.
        if grid[position] == 0:
            print(steps)
            break

        for neighbor in neighbors(grid, position):
            heappush(queue, (steps + 1, neighbor))


if __name__ == '__main__':
    grid, _, start = parse(sys.stdin.read())
    dijkstra(grid, start)
