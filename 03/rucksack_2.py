"""
--- Part Two ---

As you finish identifying the misplaced items, the Elves come to you with
another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a
badge that identifies their group. For efficiency, within each group of three
Elves, the badge is the only item type carried by all three Elves. That is, if
a group's badge is item type B, then all three Elves will have item type B
somewhere in their rucksack, and at most two of the Elves will be carrying any
other item type.

The problem is that someone forgot to put this year's updated authenticity
sticker on the badges. All of the badges need to be pulled out of the rucksacks
so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's
badges. The only way to tell which item type is the right one is by finding the
one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each
group can have a different badge item type. So, in the above example, the first
group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is
lowercase r; this must be their badges. In the second group, their badge item
type must be Z.

Priorities for these items must still be found to organize the sticker
attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for
the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What
is the sum of the priorities of those item types?
"""

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
