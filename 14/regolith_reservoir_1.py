import numpy as np
import sys


def parse(input_text: str) -> list[list[tuple[int, int], ...], ...]:
    """
    Parses the input text showing the paths of rock in the cave system into
    lists of tuples.
    Args:
        input_text: Text consisting of lines of coordinates separated by arrows
        showing the paths of rock structures within the cave.

    Returns:
        A list of lists of tuples representing the coordinates for the paths.
    """
    paths = input_text.split('\n')
    paths = [line for line in paths if len(line) > 0]
    paths = [line.split(' -> ') for line in paths]
    paths = [[tuple([int(x) for x in coordinate.split(',')])
              for coordinate in line]
             for line in paths]
    return paths


def find_borders(paths: list[list[tuple[int, int], ...], ...]
                 ) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Finds the borders of the rock structures given by a series of paths.

    Args:
        paths: A list of lists of tuples representing the coordinates for rock
        paths in a cave structure.

    Returns:
        A tuple of two tuples representing the upper-left and lower-right
        corners of the rock structure.
    """
    min_x = sorted([sorted(path) for path in paths])[0][0][0]
    max_x = sorted([sorted(path, reverse=True) for path in paths])[-1][0][0]
    min_y = sorted([sorted(path, key=lambda x: x[1])
                    for path in paths], key=lambda x: x[1])[0][0][1]
    max_y = sorted([sorted(path, key=lambda x: x[1], reverse=True)
                    for path in paths], key=lambda x: x[0][1])[-1][0][1]
    return ((min_x, min_y), (max_x, max_y))


def create_cave(paths: list[list[tuple[int, int], ...], ...],
                ul: tuple[int, int], lr: tuple[int, int]
                ) -> list[list[bool, ...], ...]:
    """
    Creates a numpy 2-D array of the cave system given a scan of rock paths.

    Args:
        paths: A list of lists of tuples representing coordinates of rock
        paths within the cave.
        ul: The upper-left corner of the rock structure.
        lr: The lower-right corner of the rock structure.

    Returns:
        A 2-D numpy array of booleans representing whether a position is rock
        or not.
    """
    shape = (lr[1] - ul[1] + 1, lr[0] - ul[0] + 1)
    cave = np.full(shape, False)
    for path in paths:
        for i in range(1, len(path)):
            curr = path[i]
            prev = path[i-1]
            x0 = min(curr[0], prev[0]) - ul[0]
            x1 = max(curr[0], prev[0]) + 1 - ul[0]
            y0 = min(curr[1], prev[1]) - ul[1]
            y1 = max(curr[1], prev[1]) + 1 - ul[1]
            cave[y0:y1, x0:x1] = True
    return cave


def pour_sand(cave: list[list[bool, ...], ...],
              ul: tuple[int, int], lr: tuple[int, int],
              sand: tuple[int, int]) -> int:
    """
    Pour sand into the cave until no more can be filled, and reports how much
    sand was used.

    Args:
        cave: A 2-D numpy array of bools.
        ul: The upper-left corner of the cave.
        lr: The lower-right corner of the cave.
        sand: The position where sand comes into the cave.

    Returns:
        An integer representing how much sand was poured into the cave.
    """
    sand = (sand[1] - ul[1], sand[0] - ul[0])
    grains = 0
    while True:
        curr = sand
        while True:
            cave[curr] = True
            down = (curr[0] + 1, curr[1])
            left = (curr[0] + 1, curr[1] - 1)
            right = (curr[0] + 1, curr[1] + 1)
            try:
                if not cave[down]:
                    cave[curr] = False
                    curr = down
                elif not cave[left]:
                    cave[curr] = False
                    curr = left
                elif not cave[right]:
                    cave[curr] = False
                    curr = right
                elif curr == sand:
                    return grains + 1
                else:
                    break
            except IndexError:
                return grains
        grains += 1


if __name__ == '__main__':
    paths = parse(sys.stdin.read())
    ul, lr = find_borders(paths)
    ul = (ul[0], 0)
    cave = create_cave(paths, ul, lr)
    print(pour_sand(cave, ul, lr, (500, 0)))
