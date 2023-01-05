import re
import sys


class Sensor:
    """
    Class for the sensor.

    Args:
        x_pos: The sensor's x position.
        y_pos: The sensor's y position.
    """
    def __init__(self, x_pos: int, y_pos: int):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def closest_beacon(self, x: int, y: int):
        """
        Initializes the closest beacon, given in x and y coordinates.

        Args:
            x: The closest beacon's x position.
            y: The closest beacon's y position.

        Returns:
            The Manhattan distance to the closest beacon.
        """
        self.x_beacon = x
        self.y_beacon = y
        self.closest = abs(self.x_pos - x) + abs(self.y_pos - y)


if __name__ == '__main__':
    row = 2_000_000
    # Initialize the sensors
    sensors = []
    beacons_on_row = set()
    for line in sys.stdin:
        coordinates = [int(x) for x in re.findall(r'[xy]=([-0-9]+)', line)]
        sensor = Sensor(coordinates[0], coordinates[1])
        sensor.closest_beacon(coordinates[2], coordinates[3])
        # This is to help subtract the coordinates on the row that are beacons
        if sensor.y_beacon == row:
            beacons_on_row.add(sensor.x_beacon)
        # If the sensor is too far away from the row, don't include it.
        if sensor.closest < abs(sensor.y_pos - row):
            continue
        sensors.append(sensor)
    # Find the intervals on the row that are in the sensor's range.
    intervals = []
    for sensor in sensors:
        dx = sensor.closest - abs(row - sensor.y_pos)
        intervals.append((sensor.x_pos - dx, sensor.x_pos + dx))
    # Determine which coordinates are not beacons.
    not_beacons = 0
    min_x = min(interval[0] for interval in intervals)
    max_x = max(interval[1] for interval in intervals)
    for x in range(min_x, max_x + 1):
        if x in beacons_on_row:
            continue
        for x1, x2 in intervals:
            if x1 <= x <= x2:
                not_beacons += 1
                break
    print(not_beacons)
