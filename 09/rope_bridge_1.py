import sys


class CB_Position:
    """
    A class for a position on a plane exhibiting Chebyshev, or "chessboard"
    distance. I.e., for two points on the board, (x1, y1) and (x2, y2), the
    distance between them is given as the max of |y2 - y1| and |x2 - x1|.
    Diagonals are from (x, y) to (x+1, y+1) are 1 instead of √2.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.history = {(x, y)}

    def move(self, direction: str, distance: int, tail: 'CB_Position' = None):
        """
        Moves in a specified direction and adds the path to the history.

        Args:
            direction: One of either 'U', 'D', 'L', or 'R' for up, down, left,
            or right.
            distance: An integer specifying how far to move in the given
            direction.
            tail: A tail to follow the movement, if there is one.
        """
        movements = {
                'U': (0, 1),
                'D': (0, -1),
                'L': (-1, 0),
                'R': (1, 0),
                'UR': (1, 1),
                'UL': (-1, 1),
                'DR': (1, -1),
                'DL': (-1, -1)
        }
        movement = movements.get(direction, (0, 0))
        for _ in range(distance):
            self.x += movement[0]
            self.y += movement[1]
            self.pos = (self.x, self.y)
            self.history.add(self.pos)
            if tail:
                tail.follow(self)

    def distance(self, x: int, y: int) -> int:
        """
        Returns the distance between the current position and the given x and
        y coordinates.

        Args:
            x: An integer.
            y: An integer.

        Returns:
            An integer measuring the distance to (x, y).
        """
        return max(abs(self.x - x), abs(self.y - y))

    def follow(self, head: 'CB_Position'):
        """
        Given another instance of CB_Position, head, will follow its position.
        The function assumes the head is never more than distance 2 away, and
        if the head is not in the same row and column, will always move
        diagonally to follow.

        Args:
            head: An instance of CB_Position.
        """
        x = head.x - self.x
        y = head.y - self.y
        move_x = (abs(x) > 1 or (abs(x) == 1 and abs(y) > 1))
        move_y = (abs(y) > 1 or (abs(y) == 1 and abs(x) > 1))
        # Lists to map each direction to 1 or -1
        dir_x = ['', 'R', 'L']
        dir_y = ['', 'U', 'D']
        move_str = ""

        if move_y:
            move_str += dir_y[(y // abs(y))]
        if move_x:
            move_str += dir_x[(x // abs(x))]
        self.move(move_str, 1)


if __name__ == '__main__':
    head = CB_Position(0, 0)
    tail = CB_Position(0, 0)
    for line in sys.stdin.readlines():
        line = line.split()
        line = (line[0], int(line[1]))
        head.move(*line, tail)
    print(len(tail.history))
