"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the
update, you need unused space of at least 30000000. You need to find a
directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the
total amount of used space) is 48381165; this means that the size of the unused
space must currently be 21618835, which isn't quite the 30000000 required by
the update. Therefore, the update still requires a directory with total size of
at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

    - Delete directory e, which would increase unused space by 584.
    - Delete directory a, which would increase unused space by 94853.
    - Delete directory d, which would increase unused space by 24933642.
    - Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up enough
space. However, directories d and / are both big enough! Between these, choose
the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the
filesystem to run the update. What is the total size of that directory?
"""

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
