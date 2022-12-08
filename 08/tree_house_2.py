"""
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know
the best spot to build their tree house: they would like to be able to see a
lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and
right from that tree; stop if you reach an edge or at the first tree that is
the same height or taller than the tree under consideration. (If a tree is
right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules
above; the proposed tree house has large eaves to keep it dry, so they wouldn't
be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    - Looking up, its view is not blocked; it can see 1 tree (of height 3).
    - Looking left, its view is blocked immediately; it can see only 1 tree (of
      height 5, right next to it).
    - Looking right, its view is not blocked; it can see 2 trees.
    - Looking down, its view is blocked eventually; it can see 2 trees (one of
      height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in
each of the four directions. For this tree, this is 4 (found by multiplying 1 *
1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of
the fourth row:

30373
25512
65332
33549
35390

    - Looking up, its view is blocked at 2 trees (by another tree with a height
      of 5).
    - Looking left, its view is not blocked; it can see 2 trees.
    - Looking down, its view is also not blocked; it can see 1 tree.
    - Looking right, its view is blocked at 2 trees (by a massive tree of
      height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the
tree house.

Consider each tree on your map. What is the highest scenic score possible for
any tree?
"""

import sys


def tree_scores(trees: list[int]) -> list[int]:
    """
    Computes visibility scores for each tree in a 2-D array, represented by its
    height. A visibility score is given by multiplying how far in each cardinal
    direction a person would be able to see before their view is blocked by a
    tree that is at least as tall as the current tree.

    Args:
        trees: A 2-D array of integers representing tree heights.

    Returns:
        A 2-D array of integers representing the visibility score at a specific
        location.
    """

    width = len(trees[0])
    height = len(trees)
    # Rotated tree array for analyzing the columns
    trees_rotated = list(zip(*trees))
    scores = [[1] * width for _ in range(height)]
    for r, row in enumerate(trees):
        for c, tree in enumerate(row):
            north = trees_rotated[c][0:r][::-1]
            south = trees_rotated[c][r+1:]
            east = row[c+1:]
            west = row[0:c][::-1]
            for view in (north, south, east, west):
                length = len(view)
                view = enumerate(view)
                try:
                    scores[r][c] *= next(i+1 for i, x in view if x >= tree)
                except StopIteration:
                    scores[r][c] *= length
    return scores


if __name__ == '__main__':
    trees = sys.stdin.read().split('\n')
    trees = [[int(x) for x in line] for line in trees if len(line) > 0]
    scores = tree_scores(trees)
    print(max([max(row) for row in scores]))
