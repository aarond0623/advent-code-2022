"""
Credit to hyper-neutrino for his implementation of the DFS algorithm and
finding distances between valves.
"""

import re
import sys
from collections import deque


class Valve:
    """
    The class for the valves.

    Args:
        **line: A line from the puzzle input used to initialize the valve.
            If this is set, the rest of the args will be overridden.
        **name: The name of the valve.
        **flow: The flow rate of the valve.
        **targets: A list of other target valve objects.
    """
    cache = {}  # Cache for the depth-first search

    @classmethod
    def init_valves(cls, text: str):
        """
        Initializes the valves from text.

        Args:
            text: The input puzzle text.
        """
        cls.valves = {}  # A dictionary of all valves.
        cls.positive_valves = []  # All valves with flow > 0
        cls.check_valves = []  # Positive valves + AA
        for line in text:
            valve = Valve(line=line)
            cls.valves[valve.name] = valve
            if valve.name == 'AA':
                cls.check_valves.append(valve)
            if valve.flow > 0:
                cls.check_valves.append(valve)
                cls.positive_valves.append(valve)
        # Convert the list of strings into a lsit of objects.
        for valve in cls.valves.values():
            valve.targets = [cls.valves[x] for x in valve.targets]
        # Generate an index list for use by the bitmask later
        cls.indices = {}
        for index, valve in enumerate(cls.positive_valves):
            cls.indices[valve.name] = index

    @classmethod
    def generate_distances(cls):
        """
        Generates a dictionary of distances for each valve in the list of
        valves to be checked.
        """
        for valve in cls.check_valves:
            valve.dists[valve.name] = 0
            valve.dists['AA'] = 0
            visited = {valve.name}

            queue = deque([(0, valve.name)])

            while queue:
                dist, pos = queue.popleft()
                for target in cls.valves[pos].targets:
                    if target.name in visited:
                        continue
                    visited.add(target.name)
                    if target.flow:
                        valve.dists[target.name] = dist + 1
                    queue.append((dist + 1, target.name))

            # Delete the valve itself and AA from our distances so we don't
            # check them.
            del valve.dists[valve.name]
            if valve.name != 'AA':
                del valve.dists['AA']

    @classmethod
    def dfs(cls, time, name, bitmask):
        """
        Depth-first search to find the best possible pressure release.

        Args:
            time: The remaining time.
            name: The name of the current valve.
            bitmask: A number representing the current state of the valves.
        """
        valve = cls.valves[name]
        # Cache values to reduce search time.
        if (time, name, bitmask) in cls.cache:
            return cls.cache[(time, name, bitmask)]
        pressure = 0
        for target in valve.dists:
            # Create a bitmask where 1 is open and 0 is closed.
            bit = 1 << cls.indices[target]
            if bitmask & bit:  # Valve is already open.
                continue
            remtime = time - valve.dists[target] - 1
            if remtime <= 0:
                continue
            new_pressure = cls.dfs(remtime, target, bitmask | bit)
            new_pressure += cls.valves[target].flow * remtime
            pressure = max(pressure, new_pressure)
        cls.cache[(time, name, bitmask)] = pressure
        return pressure

    def __init__(self, **kwargs):
        self.dists = {}  # Dictionary of valve names and distances
        try:
            self.parse(kwargs['line'])
        except KeyError:
            self.name = kwargs.get('name', '')
            self.flow = kwargs.get('flow', 0)
            self.targets = kwargs.get('targets', [])

    def __eq__(self, other):
        return self.name == other.name

    def parse(self, line: str):
        """
        Parses a line from the puzzle into the valve values.

        Args:
            line: A line of puzzle input.
        """
        names = re.findall(r'([A-Z]{2})', line)
        self.flow = int(re.search(r'rate=([0-9]+);', line)[1])
        self.name = names[0]
        self.targets = names[1:]


if __name__ == '__main__':
    Valve.init_valves(sys.stdin.readlines())
    Valve.generate_distances()
    print(Valve.dfs(30, 'AA', 0))
