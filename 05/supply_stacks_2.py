"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the
process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly
wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air
conditioning, leather seats, an extra cup holder, and the ability to pick up
and move multiple crates at once.

Again considering the example above, the crates begin in the same
configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means that
those three moved crates stay in the same order, resulting in this new
configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order
as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's
crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different
order: MCD.

Before the rearrangement process finishes, update your simulation so that the
Elves know where they should stand to be ready to unload the final supplies.
After the rearrangement procedure completes, what crate ends up on top of each
stack?
"""

import sys
from supply_stacks_1 import *


def move_crates_improved(
    crates: list[list[str]], instruction: dict[str, int]) -> None:
    """
    Moves crates in a 2-D array according to an instruction consisting of a
    move quantity, a from stack, and a to stack. When multiple crates are
    moved, they retain their order.

    Args:
        crates: A two-dimensional array of single-character strings.
        instruction: A dict of values for qty, from_stack, and to_stack.
    """

    qty = instruction['qty']
    from_stack = instruction['from_stack'] - 1
    to_stack = instruction['to_stack'] - 1
    i = len(crates[from_stack]) - qty

    crates[to_stack] += crates[from_stack][i:]
    crates[from_stack] = crates[from_stack][:i]


if __name__ == '__main__':
    input_text = sys.stdin.read().split('\n')
    for i, line in enumerate(input_text):
        if line[0:2] == ' 1':
            stack_text = input_text[0:i]
            instruction_text = input_text[i+2:]
    crates = initialize_crates(stack_text)
    for instruction in instruction_text:
        move_crates_improved(crates, parse_instruction(instruction))
    print("".join([x[-1] for x in crates]))
