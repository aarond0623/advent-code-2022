import sys


def find_repeat(input_string: str) -> int:
    """
    Returns the first position in a string where there is a duplicate
    character.

    Args:
        input_string: A string of characters.

    Returns:
        The integer for the position of the first character that contains a
        duplicate elsewhere in the string. If there is no duplicate, returns
        -1.
    """
    for i in range(len(input_string) - 1):
        for j in range(i+1, len(input_string)):
            if ord(input_string[i]) ^ ord(input_string[j]) == 0:
                return i
    return -1


if __name__ == '__main__':
    signal = sys.stdin.readline()
    i = 0
    while True:
        result = find_repeat(signal[i:i+4])
        if result == -1:
            print(i + 4)
            break
        # Skip to after first repeated character so we don't recheck the same
        # duplicate.
        i += result + 1
