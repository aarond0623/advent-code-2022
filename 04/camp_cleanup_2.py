"""
It seems like there is still quite a bit of duplicate work planned.
Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap,
while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do
overlap:

    - 5-7,7-9 overlaps in a single section, 7.
    - 2-8,3-7 overlaps all of the sections 3 through 7.
    - 6-6,4-6 overlaps in a single section, 6.
    - 2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""

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
