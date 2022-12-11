import sys
from typing import Callable


class Monkey:
    """
    A class for each monkey playing monkey-in-the-middle.

    Args:
        items: A list of integers representing the worry level of various
        items.
        operation: A function to perform on an item when inspecting it. The
        function should return an integer representing the new worry level.
        test: A test to perform on an item after inspecting it. Should return
        either True or False.
        monkey_true: The monkey to throw the item to if the test function
        returns True.
        monkey_false: The monkey to throw the item to if the test function
        returns False.
    """
    def __init__(
            self,
            items: list[int],
            operation: Callable[[int], int],
            test: Callable[[int], bool],
            monkey_true: 'Monkey' = None,
            monkey_false: 'Monkey' = None):
        self.items = items
        self.operation = operation
        self.test = test
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspections = 0

    def inspect(self, item: int) -> int:
        self.inspections += 1
        return self.operation(item)

    def relief(self, item: int) -> int:
        """
        After a monkey inspects an item and doesn't damage it, the worry
        level decreases.
        """
        return item // 3

    def transfer(self, item: int):
        result = self.test(item)
        # We don't remove the items here so that we are not mutating the list
        # while it is being inspected.
        if result:
            self.monkey_true.items.append(item)
        else:
            self.monkey_false.items.append(item)

    def inspect_items(self):
        # Every item will be thrown to some other monkey, so we will store the
        # original length of the items list, then throw it away at the end. If
        # the monkey throws to itself, that item will be preserved.
        items_len = len(self.items)
        for item in self.items:
            item = self.inspect(item)
            item = self.relief(item)
            self.transfer(item)
        self.items = self.items[items_len:]


def parse(input_text: str, monkey_type) -> list['Monkey']:
    """Parses the puzzle input and returns a list of monkeys."""
    monkeys = []
    for line in input_text:
        match line.split():
            case ['Monkey', _]:
                curr_monk = []
            case ['Starting', 'items:', *items]:
                for i, n in enumerate(items):
                    items[i] = int(''.join([x for x in n if x.isdigit()]))
                curr_monk.append(items)
            case ['Operation:', *op]:
                exec('curr_monk.append(lambda old: ' + ' '.join(op[2:]) + ')')
            case ['Test:', *test]:
                exec('curr_monk.append(lambda x: x %' + test[-1] + '==0)')
            case ['If', 'true:', *val]:
                curr_monk.append(int(val[-1]))
            case ['If', 'false:', *val]:
                curr_monk.append(int(val[-1]))
                monkeys.append(curr_monk)
            case _:
                pass
    monkey_list = []
    for monkey in monkeys:
        monkey_list.append(monkey_type(*monkey[0:3]))
    for i, monkey in enumerate(monkeys):
        monkey_list[i].monkey_true = monkey_list[monkey[3]]
        monkey_list[i].monkey_false = monkey_list[monkey[4]]
    return monkey_list


if __name__ == '__main__':
    monkeys = parse(sys.stdin.readlines(), Monkey)
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_items()
    monkey_business = sorted([monkey.inspections for monkey in monkeys])[::-1]
    print(monkey_business[0] * monkey_business[1])
