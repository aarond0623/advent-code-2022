import sys
from camp_cleanup_1 import parse_range


if __name__ == '__main__':
    total = 0
    for line in sys.stdin:
        pair = list(map(parse_range, line.split(',')))
        # Sort first by the first element, and then the inverse of the second
        # element. This ensures that if the first elements in the pair are
        # equal, the first range is always wider.
        pair.sort(key=lambda x: (x[0], -x[1]))
        if pair[0][1] >= pair[1][0]:  # Ranges overlap.
            total += 1
    print(total)
