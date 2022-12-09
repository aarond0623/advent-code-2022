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
