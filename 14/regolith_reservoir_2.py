import sys
from regolith_reservoir_1 import *


if __name__ == '__main__':
    paths = parse(sys.stdin.read())
    ul, lr = find_borders(paths)
    # The floor will extend 5 units past the floor in both directions, and 2
    # units under the lowest point.
    ul = (0, 0)
    lr = (lr[0] + 200, lr[1] + 2)
    cave = create_cave(paths, ul, lr)
    # Draw the floor
    cave[-1] = True
    print(pour_sand(cave, ul, lr, (500, 0)))
