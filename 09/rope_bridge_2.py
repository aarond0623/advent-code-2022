import sys
from rope_bridge_1 import *

MAX_KNOTS = 10


if __name__ == '__main__':
    rope = [CB_Position(0, 0) for _ in range(MAX_KNOTS)]
    for line in sys.stdin.readlines():
        line = line.split()
        for _ in range(int(line[1])):
            rope[0].move(line[0], 1)
            for i, knot in enumerate(rope[1:]):
                knot.follow(rope[i])
    print(len(rope[MAX_KNOTS - 1].history))
