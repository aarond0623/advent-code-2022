import sys
from monkey_in_the_middle_1 import *

class BadMonkey(Monkey):
    def __init__(self, *args, **kwargs):
        self.divisor = 1
        super().__init__(*args, **kwargs)

    def relief(self, item):
        """No longer provides relief, but we will use the function to
        mod by divisor."""
        return item % self.divisor


def parse2(input_text: str, monkey_type) -> (list['BadMonkey'], int):
    divisor = 1
    # Multiply all test numbers together, so that any number mod it will retain
    # divisibility tests with all monkeys.
    for line in input_text:
        match line.split():
            case ['Test:', *test]:
                divisor *= int(test[-1])
    return (parse(input_text, monkey_type), divisor)


if __name__ == '__main__':
    monkeys = parse2(sys.stdin.readlines(), BadMonkey)
    divisor = monkeys[1]
    monkeys = monkeys[0]
    for monkey in monkeys:
        monkey.divisor = divisor
    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect_items()
    monkey_business = sorted([monkey.inspections for monkey in monkeys])[::-1]
    print(monkey_business[0] * monkey_business[1])
