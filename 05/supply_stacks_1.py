"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from
the ships. Supplies are stored in stacks of marked crates, but because the
needed supplies are buried under many other crates, the crates need to be
rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To
ensure none of the crates get crushed or fall over, the crane operator will
rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where, and they
want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the
rearrangement procedure (your puzzle input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates:
crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates;
from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a
single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a
quantity of crates is moved from one stack to a different stack. In the first
step of the above rearrangement procedure, one crate is moved from stack 2 to
stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates are
moved one at a time, so the first crate to be moved (D) ends up below the
second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are
moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1       3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in
this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3,
so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each
stack?
"""

import re
import sys


def parse_instruction(instruction: str) -> dict[str, int]:
    """
    Parses instructions for moving the crates and returns a dictionary of the
    relevant values.

    Args:
        instruction: A string in the form of "move n from x to y".

    Returns:
        A dictionary in the form of {qty: n, from_stack: x, to_stack: y}.
    """
    match = re.search('move ([0-9]+) from ([0-9]+) to ([0-9]+)', instruction)
    try:
        qty = int(match.group(1))
        from_stack = int(match.group(2))
        to_stack = int(match.group(3))
    except AttributeError:  # Matches weren't found
        return {'qty': 0, 'from_stack': 0, 'to_stack': 0}
    return {'qty': qty, 'from_stack': from_stack, 'to_stack': to_stack}


def move_crates(crates: list[list[str]], instruction: dict[str, int]) -> None:
    """
    Moves crates in a 2-D array according to an instruction consisting of a
    move quantity, a from stack, and a to stack.

    Args:
        crates: A two-dimensional array of single-character strings.
        instruction: A dict of values for qty, from_stack, and to_stack.
    """
    for _ in range(instruction['qty']):
        # Subtract 1 in order to 0 index the array.
        from_stack = instruction['from_stack'] - 1
        to_stack = instruction['to_stack'] - 1
        crates[to_stack].append(crates[from_stack].pop())


def initialize_crates(crates: list[str]) -> list[list[str]]:
    """
    Initializes the stacks of crates using an input list of strings where
    crates are represented as vertically stacked boxes in the form of [A],
    where each box holds a single character.

    Args:
        crates: A list of strings representing rows in the various stacks.

    Returns:
        A 2-D array where each element is a stack of crates, with the
        bottom-most crate first.
    """
    max_len = len(crates[-1])
    crates = [row.ljust(max_len) for row in crates]
    crates = [[row[i] for i in range(1, max_len, 4)] for row in crates]
    crates = list(zip(*crates[::-1]))
    crates = [[x for x in row if x != ' '] for row in crates]
    return crates


if __name__ == '__main__':
    input_text = sys.stdin.read().split('\n')
    for i, line in enumerate(input_text):
        if line[0:2] == ' 1':
            stack_text = input_text[0:i]
            instruction_text = input_text[i+2:]
    crates = initialize_crates(stack_text)
    for instruction in instruction_text:
        move_crates(crates, parse_instruction(instruction))
    print("".join([x[-1] for x in crates]))
