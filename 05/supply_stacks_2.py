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
