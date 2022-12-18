import sys
from functools import cmp_to_key
from distress_signal_1 import *


# Credit to FredFoo from StackOverflow for this function
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare


if __name__ == '__main__':
    signals = [eval(x) for x in sys.stdin.read().split('\n') if x != '']
    signals += [[[2]], [[6]]]
    sort_key = cmp_to_key(make_comparator(test_packets))
    signals.sort(key=sort_key)
    print((signals.index([[2]]) + 1) * (signals.index([[6]]) + 1))
