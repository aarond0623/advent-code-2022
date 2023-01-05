import re
import sys
from beacon_1 import *


class SensorBorders(Sensor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def distance(self, x: int, y: int) -> int:
        """
        Returns the Manhattan distance from the sensor to an arbitrary point.

        Args:
            x: The x coordinate of the point.
            y: The y coordinate of the point.

        Returns:
            The Manhattan distance from the sensor to the point.
        """
        return abs(self.x_pos - x) + abs(self.y_pos - y)

    def y_intercepts(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Returns a tuple of two tuples representing the y-intercepts of the
        borders around the sensor that may contain beacons.

        Returns:
            ((a, b), (c, d)) where a and b are the y-intercepts for the borders
            with positive slope, and c and d are the y-intercepts for the
            borders with negative slope
        """
        # y-intercepts, adjusted by 1 to be outside the beacon range.
        a = self.y_pos - self.x_pos - 1
        b = self.y_pos - self.x_pos + 1
        c = self.y_pos + self.x_pos - 1
        d = self.y_pos + self.x_pos + 1
        try:
            a -= self.closest
            b += self.closest
            c -= self.closest
            d += self.closest
        except NameError:
            pass
        return ((a, b), (c, d))


if __name__ == '__main__':
    # The free point not covered by the borders of any sensor will be at the
    # intersection of one of these lines just outside the sensor's borders.
    # We will find all the points where two lines intersect and check if they
    # are near a sensor.
    min_coord = 0
    max_coord = 4_000_000
    pos_intercepts = set()
    neg_intercepts = set()
    # Initialize the sensors
    sensors = []
    for line in sys.stdin:
        coordinates = [int(x) for x in re.findall(r'[xy]=([-0-9]+)', line)]
        sensor = SensorBorders(coordinates[0], coordinates[1])
        sensor.closest_beacon(coordinates[2], coordinates[3])
        sensors.append(sensor)
        intercepts = sensor.y_intercepts()
        pos_intercepts.update(intercepts[0])
        neg_intercepts.update(intercepts[1])

    # Analyze the intersection points
    for a in pos_intercepts:
        for b in neg_intercepts:
            x, y = (b - a) // 2, (a + b) // 2
            if all(min_coord < coord < max_coord for coord in (x, y)):
                if all(s.distance(x, y) > s.closest for s in sensors):
                    print(max_coord * x + y)
