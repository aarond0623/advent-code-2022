"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted
carefully in a grid. The Elves explain that a previous expedition planted these
trees as a reforestation effort. Now, they're curious if this would be a good
location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house
hidden. To do this, you need to count the number of trees that are visible from
outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height
of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0
is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid
are shorter than it. Only consider trees in the same row or column; that is,
only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are
already on the edge, there are no trees to block the view. In this example,
that only leaves the interior nine trees to consider:

    - The top-left 5 is visible from the left and top. (It isn't visible from
      the right or bottom since other trees of height 5 are in the way.)
    - The top-middle 5 is visible from the top and right.
    - The top-right 1 is not visible from any direction; for it to be visible,
      there would need to only be trees of height 0 between it and an edge.
    - The left-middle 5 is visible, but only from the right.
    - The center 3 is not visible from any direction; for it to be visible,
      there would need to be only trees of at most height 2 between it and an
      edge.
    - The right-middle 3 is visible from the right.
    - In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a
total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""

import sys


def find_visible(trees: list[int]) -> list[bool]:
    """
    Finds which trees are visible in a 2-D forest. Trees are represented by
    integers for their height. A tree is visible if it is the tallest tree from
    any edge.

    Args:
        trees: A two-dimensional array of integers representing tree height.

    Returns:
        A two-dimensional array of booleans representing which trees are
        visible in the original array.
    """
    width = len(trees[0])
    height = len(trees)
    # All trees on the edge are visible by default.
    visible = [[True] + [False] * (width - 2) + [True] for _ in range(height)]
    visible[0] = [True] * width
    visible[-1] = [True] * width
    for r, row in enumerate(trees):
        for c, tree in enumerate(row):
            if visible[r][c]:
                continue
            if tree > max(row[0:c]) or tree > max(row[c+1:]):
                visible[r][c] = True
    # Rotate array and check columns
    trees_rotated = list(zip(*trees))
    for c, col in enumerate(trees_rotated):
        for r, tree in enumerate(col):
            if visible[r][c]:
                continue
            if tree > max(col[0:r]) or tree > max(col[r+1:]):
                visible[r][c] = True
    return visible


if __name__ == '__main__':
    trees = sys.stdin.read().split('\n')
    trees = [[int(x) for x in line] for line in trees if len(line) > 0]
    visible = find_visible(trees)
    print(sum([sum([1 for x in row if x]) for row in visible]))
