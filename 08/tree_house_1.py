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
