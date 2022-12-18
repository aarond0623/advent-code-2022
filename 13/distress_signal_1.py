import sys


def get_packets(packet1: str, packet2: str) -> tuple[list, list]:
    """
    A parser that takes in two strings, both typeset as lists, and returns a
    tuple of both lists. The lists may contain integers or other lists.

    Args:
        packet1: A string representing the first packet.
        packet2: A string representing the second packet.

    Returns:
        A tuple of two lists.
    """
    packet1 = eval(packet1)
    packet2 = eval(packet2)
    return (packet1, packet2)


def test_packets(left: list, right: list) -> bool:
    """
    Tests whether two packets, left and right, are ordered correctly based on
    the puzzle logic.

    Args:
        left: The left packet.
        right: The right packet.

    Returns:
        True if the packets are in the correct order, False if not, and None
        if the order is undetermined.
    """
    # Always deal with lists as input
    if type(left) is not list:
        left = [left]
    if type(right) is not list:
        right = [right]
    for l, r in zip(left, right):
        # If there's a list within the list, recursively solve
        if (type(l), type(r)) != (int, int):
            result = test_packets(l, r)
            # If we cannot determine the order yet.
            if result is not None:
                return result
        elif l == r:
            continue
        else:
            return l < r
    # All numbers were the same, test the lengths
    else:
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
        else:
            return None


if __name__ == '__main__':
    input_text = sys.stdin.read().split('\n\n')
    input_text = [x.split('\n')[0:2] for x in input_text]
    total = 0
    for i, pair in enumerate(input_text):
        if test_packets(*get_packets(*pair)):
            # Puzzle is 1-indexed
            total += (i + 1)
    print(total)
