import re
import sys
from collections import deque
from elephants_1 import *


if __name__ == '__main__':
    Valve.init_valves(sys.stdin.readlines())
    Valve.generate_distances()

    bitmask = (1 << len(Valve.positive_valves)) - 1
    pressure = 0

    for i in range((bitmask + 1) // 2):
        new_pressure = Valve.dfs(26, 'AA', i)
        new_pressure += Valve.dfs(26, 'AA', bitmask ^ i)
        pressure = max(pressure, new_pressure)

    print(pressure)
