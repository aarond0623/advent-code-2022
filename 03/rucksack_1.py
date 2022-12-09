import string
import sys


def find_rucksack_duplicate(rucksack_string):
    """
    Finds a duplicate item in a rucksack represented by a string of characters.

    Args:
        rucksack_string: A string of letters where the first half of the string
        represents one compartment of the rucksack, and the second, the other
        compartment of the rucksack.

    Returns:
        The first character that is found in both compartments.
    """

    compartment1 = rucksack_string[0:len(rucksack_string) // 2]
    compartment2 = rucksack_string[len(rucksack_string) // 2:]

    for letter in compartment1:
        if letter in compartment2:
            return letter


def get_priority(item):
    """
    Gets the priority of an item, represented by a single character.

    Args:
        item: A single character, one of A-Z or a-z.

    Returns:
        The priority of the item, where a-z have a prioty of 1-26, and A-Z have
        a priotiy of 27-52. If an item is not a letter, the function returns
        None.
    """

    try:
        return string.ascii_letters.index(item) + 1
    except ValueError:  # Not a letter
        return None


if __name__ == '__main__':
    total = 0
    for line in sys.stdin:
        total += get_priority(find_rucksack_duplicate(line))
    print(total)
