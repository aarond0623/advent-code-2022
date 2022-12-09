import sys


def parse_range(range_string: str) -> tuple[int, int]:
    """
    Parses a range given in the form X-Y and returns a tuple of the two
    numbers, (X, Y).

    Args:
        range_string: A string in the form of X-Y, where X and Y are integers.

    Returns:
        A tuple of two integers, (X, Y).
    """
    return tuple(map(int, range_string.split('-')))


if __name__ == '__main__':
    total = 0
    for line in sys.stdin:
        pair = list(map(parse_range, line.split(',')))
        # Sort first by the first element, and then the inverse of the second
        # element. This ensures that if the first elements in the pair are
        # equal, the first range is always wider.
        pair.sort(key=lambda x: (x[0], -x[1]))
        if pair[0][1] >= pair[1][1]:  # First range encompasses second
            total += 1
    print(total)
