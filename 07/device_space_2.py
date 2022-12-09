import sys
from device_space_1 import *


def find_smallest_deletion(folder: 'File', space: int, candidates: list[int]):
    """
    Finds the size of the smallest folder needed to free up a given amount of
    space in a directory tree.

    Args:
        folder: The current folder to search.
        space: The amount of free space that needs to be freed.
        candidates: A list of integers representing the sizes of folders that
        could be deleted.

    Returns:
        An integer representing the smallest size of all candidate folders.
    """
    subfolders = folder.contents
    subfolders = [subfolders[x] for x in subfolders if subfolders[x].is_dir]
    size = folder.get_size()
    if size >= space:
        candidates.append(size)
    for subfolder in subfolders:
        find_smallest_deletion(subfolder, space, candidates)
    return min(candidates)


if __name__ == '__main__':
    instruction = []
    dir_tree = [File('/')]  # Root directory
    for line in sys.stdin:
        if line[0] == '$' and len(instruction) > 0:
            parse_instruction(instruction, dir_tree)
            instruction = [line]  # Start of new instruction list.
        else:
            instruction.append(line)
    # Parse final instruction
    if len(instruction) > 0:
        parse_instruction(instruction, dir_tree)
    space = 30000000 - (70000000 - dir_tree[0].get_size())
    print(find_smallest_deletion(dir_tree[0], space, []))
