import sys
from rucksack_1 import get_priority


def find_badge(sack1, sack2, sack3):
    """
    Finds a badge in a set of rucksacks represented by strings of characters by
    finding the first character alphabetically shared by all three strings.

    Args:
        sack1: A string
        sack2: A string
        sack3: A string

    Returns:
        The first character that is found in all three strings.
    """
    # Convert strings to sets so we only have to check each letter once.
    sack1, sack2, sack3 = list(map(lambda x: set(x), [sack1, sack2, sack3]))
    for letter in sack1:
        if letter in sack2 and letter in sack3:
            return letter


if __name__ == '__main__':
    total = 0
    while lines := [sys.stdin.readline().rstrip() for _ in range(3)]:
        try:
            total += get_priority(find_badge(*lines))
        except TypeError:  # End of File
            break
    print(total)
