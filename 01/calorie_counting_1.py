import sys


def summarize_list(list_text):
    """
    Summarizes a list of numbers given as a string and separated by new lines.

    Args:
        list_text: Text of groups of numbers separated by blank lines.
    Returns:
        A list of the sum of each group of numbers.
    """
    summed_list = []
    number_list = list_text.split('\n')
    total = 0
    for number in number_list:
        for func in int, float:  # Try to convert to both, but prefer integer.
            try:
                total += func(number)
                break
            except ValueError:
                continue
        else:  # This was a blank line, or not a number.
            summed_list.append(total)
            total = 0
    return summed_list


if __name__ == '__main__':
    summed_list = summarize_list(sys.stdin.read())
    print(max(summed_list))
