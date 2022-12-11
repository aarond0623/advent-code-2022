import sys


class CRT:
    """A class for the cathode-ray tube screen."""
    def __init__(self):
        self.x_register = 1
        self.cycle = 0
        self.total_signal_strength = 0

    def noop(self):
        """Does nothing. Takes 1 cycle."""
        self.tick()

    def addx(self, val):
        """Adds val to x register. Takes 2 cycles."""
        self.noop()
        self.tick()
        self.x_register += val

    def tick(self):
        self.cycle += 1
        if (self.cycle + 20) % 40 == 0:
            self.total_signal_strength += self.x_register * self.cycle


if __name__ == '__main__':
    crt = CRT()
    for line in sys.stdin:
        line = line.split()
        match line[0]:
            case 'noop':
                crt.noop()
            case 'addx':
                crt.addx(int(line[1]))
    print(crt.total_signal_strength)
