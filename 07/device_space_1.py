"""
--- Day 7: No Space Left On Device ---

You can hear birds chirping and raindrops hitting leaves as the expedition
proceeds. Occasionally, you can even hear much louder sounds in the distance;
how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its
communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting
terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

The filesystem consists of a tree of files (plain data) and directories (which
can contain other directories or files). The outermost directory is called /.
You can navigate around the filesystem, moving into or out of directories and
listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed,
very much like some modern computers:

    - cd means change directory. This changes which directory is the current
      directory, but the specific result depends on the argument:
        - cd x moves in one level: it looks in the current directory for the
          directory named x and makes it the current directory.
        - cd .. moves out one level: it finds the directory that contains the
          current directory, then makes that directory the current directory.
        - cd / switches the current directory to the outermost directory, /.
    - ls means list. It prints out all of the files and directories immediately
      contained by the current directory:
        - 123 abc means that the current directory contains a file named abc
          with size 123.
        - dir xyz means that the current directory contains a directory named
          xyz.

Given the commands and output in the example above, you can determine that the
filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

Here, there are four directories: / (the outermost directory), a and d (which
are in /), and e (which is in a). These directories also contain files of
various sizes.

Since the disk is full, your first step should probably be to find directories
that are good candidates for deletion. To do this, you need to determine the
total size of each directory. The total size of a directory is the sum of the
sizes of the files it contains, directly or indirectly. (Directories themselves
do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

    - The total size of directory e is 584 because it contains a single file i
      of size 584 and no other directories.
    - The directory a has total size 94853 because it contains files f (size
      29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a
      contains e which contains i).
    - Directory d has total size 24933642.
    - As the outermost directory, / contains every file. Its total size is
      48381165, the sum of the size of every file.

To begin, find all of the directories with a total size of at most 100000, then
calculate the sum of their total sizes. In the example above, these directories
are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this
example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the
sum of the total sizes of those directories?
"""

import sys


class File:
    """
    A file with a name and size. Can be either a directory or file. If an item
    is a file, it will have a size and no contents. Conversely, a directory
    will have no size and may or may not contain contents.

    Args:
        name: The name of the file or directory.
        size: An integer representing this file's inherent size. This is not
        the actual size of the directory, if this is a directory; size should
        be gotten through the get_size() method.

    Attributes:
        name: The name of the file or directory.
        contents: A dict of file/directory names and the File class itself.
        size: An integer representing this file's inherent size.
        is_dir: True if the file has contents, False otherwise.
    """
    def __init__(self, name: str, size: int = 0):
        self.name = name
        self.contents = dict()
        self.is_dir = False  # Default to not being a directory.
        self.size = size

    def get_size(self):
        """Returns the size of this file or directory."""
        size = sum([item.get_size() for item in self.contents.values()])
        size += self.size
        return size

    def add(self, item: 'File'):
        """
        Adds a file to the directory contents.

        Args:
            item: A file or directory object.
        """
        # Ensure files don't have contents
        assert self.size == 0, "This is a file, not a directory."
        self.contents[item.name] = item
        self.is_dir = True


def parse_instruction(instruction: list[str], dir_tree: list['File']):
    """
    Parses a shell instruction given as a list of strings including the actual
    instruction, starting with a dollar sign ($) and the output, if any, of
    that instruction.

    Args:
        instruction: A list of string including the command and any output.
        dir_tree: A list of the current branch of the directory tree, with the
        most recent item last.
    """
    match instruction[0].split():
        case '$', 'cd', '/': dir_tree = dir_tree[0]
        case '$', 'cd', '..': dir_tree.pop()
        case '$', 'cd', folder:
            try:
                dir_tree.append(dir_tree[-1].contents[folder])
            except KeyError:
                dir_tree.add(File(folder))
                dir_tree.append(dir_tree[-1].contents[folder])
        case '$', 'ls':
            for line in instruction[1:]:
                line = line.split()
                name = line[1]
                size = (lambda x: 0 if x == 'dir' else int(x))(line[0])
                dir_tree[-1].add(File(name, size=size))
        case _:
            pass


def find_under_size(folder: 'File', max_size: int, total_size: int = 0):
    """
    Finds the total size of all folders under a certain size in a directory.

    Args:
        folder: The current folder to search.
        max_size: The maximum size to consider in our search.
        total_size: The total size found so far.

    Returns:
        The sum of the sizes of all folders under the maximum size.
    """
    subfolders = folder.contents
    subfolders = [subfolders[x] for x in subfolders if subfolders[x].is_dir]
    size = folder.get_size()
    if size > max_size:
        size = 0
    total_size += size  # Update total size
    for subfolder in subfolders:
        total_size = find_under_size(subfolder, max_size, total_size)
    return total_size


if __name__ == '__main__':
    instruction = []
    dir_tree = [File('/')]  # Root directory
    for line in sys.stdin:
        if line[0] == '$' and len(instruction) > 0:
            parse_instruction(instruction, dir_tree)
            instruction = [line]  # Start a new instruction list.
        else:
            instruction.append(line)
    # Parse final instructions:
    if len(instruction) > 0:
        parse_instruction(instruction, dir_tree)
    total_size = find_under_size(dir_tree[0], 100000)
    print(total_size)
