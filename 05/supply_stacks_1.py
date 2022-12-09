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
