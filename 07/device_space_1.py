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
