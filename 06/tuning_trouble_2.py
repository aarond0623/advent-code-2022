"""
--- Part Two ---

Your device's communication system is correctly detecting packets, but still
isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it
consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above
examples:

    - mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    - bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    - nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    - nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    - zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message
marker is detected?
"""

import sys
from tuning_trouble_1 import *


if __name__ == '__main__':
    signal = sys.stdin.readline()
    i = 0
    while True:
        result = find_repeat(signal[i:i+14])
        if result == -1:
            print(i + 14)
            break
        i += result + 1
