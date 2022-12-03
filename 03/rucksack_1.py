"""
--- Day 3: Rucksack Reorganization ---

One Elf has the important job of loading all of the rucksacks with supplies for
the jungle journey. Unfortunately, that Elf didn't quite follow the packing
instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant
to go into exactly one of the two compartments. The Elf that did the packing
failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your
puzzle input), but they need your help finding the errors. Every item type is
identified by a single lowercase or uppercase letter (that is, a and A refer to
different types of items).

The list of items for each rucksack is given as characters all on a single
line. A given rucksack always has the same number of items in each of its two
compartments, so the first half of the characters represent items in the first
compartment, while the second half of the characters represent items in the
second compartment.

For example, suppose you have the following list of contents from six
rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

    - The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which
      means its first compartment contains the items vJrwpWtwJgWr, while the
      second compartment contains the items hcsFMMfFFhFp. The only item type
      that appears in both compartments is lowercase p.
    - The second rucksack's compartments contain jqHRNqRjqzjGDLGL and
      rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is
      uppercase L.
    - The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the
      only common item type is uppercase P.
    - The fourth rucksack's compartments only share item type v.
    - The fifth rucksack's compartments only share item type t.
    - The sixth rucksack's compartments only share item type s.

To help prioritize item rearrangement, every item type can be converted to a
priority:

    - Lowercase item types a through z have priorities 1 through 26.
    - Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both
compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19
(s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is
the sum of the priorities of those item types?
"""

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
