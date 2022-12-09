import sys
from calorie_counting_1 import summarize_list


if __name__ == '__main__':
    summed_list = summarize_list(sys.stdin.read())
    print(sum(sorted(summed_list, reverse=True)[0:3]))
