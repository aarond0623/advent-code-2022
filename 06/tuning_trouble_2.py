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
