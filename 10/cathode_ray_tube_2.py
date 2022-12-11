import sys
from cathode_ray_tube_1 import *


class CRT_Draw(CRT):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.display = [['.'] * width for _ in range(height)]

    def tick(self):
        y = self.cycle // self.width
        x = self.cycle % self.width
        # Check if the sprite is no more than 1 location away.
        if abs(self.x_register - x) <= 1:
            self.display[y][x] = '#'
        self.cycle += 1

    def draw_display(self):
        for i in range(self.height):
            print("".join(self.display[i]))



if __name__ == '__main__':
    crt = CRT_Draw(40, 6)
    for line in sys.stdin:
        line = line.split()
        match line[0]:
            case 'noop':
                crt.noop()
            case 'addx':
                crt.addx(int(line[1]))
    crt.draw_display()
