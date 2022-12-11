import operator
from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()


class Monkey:
    def __init__(self, number, items, operation, pow, constant, test, throw_true, throw_false):
        self.number = number
        self.items = items.copy()
        self.operation = operation
        self.pow = pow
        self.constant = constant
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspected = 0


monkeys_part_1 = []
monkeys_part_2 = []

for i in range(0, len(lines), 7):
    c = lines[i:i + 7]
    number = int(c[0].split('Monkey ')[1].strip()[:-1])
    starting_items = list(
        map(lambda x: int(x), c[1].split(': ')[1].strip().split(', ')))
    operation, other = c[2].split(': ')[1].split('old ')[1].strip().split(' ')
    test = int(c[3].split(': ')[1].strip().split('divisible by ')[1])
    true = int(c[4].split(': ')[1].strip().split('throw to monkey ')[1])
    false = int(c[5].split(': ')[1].strip().split('throw to monkey ')[1])
    pow = other == 'old'
    constant = 0 if pow else int(other)
    m = Monkey(number, starting_items, operation,
               pow, constant, test, true, false)
    m2 = Monkey(number, starting_items, operation,
                pow, constant, test, true, false)
    monkeys_part_1.append(m)
    monkeys_part_2.append(m2)


def round(monkeys, worry_div):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1

            new = 0

            if monkey.pow:
                new = item * item
            else:
                if monkey.operation == '*':
                    new = item * monkey.constant
                else:
                    new = item + monkey.constant

            if worry_div != 3:
                if new > worry_div:
                    new = new % worry_div
            else:
                new = new // worry_div

            if new % monkey.test == 0:
                monkeys[monkey.throw_true].items.append(new)
            else:
                monkeys[monkey.throw_false].items.append(new)

        monkey.items.clear()


def main():
    for i in range(0, 20):
        round(monkeys_part_1, 3)

    d = reduce(lambda x, y: x * y,
               [monkey.test for monkey in monkeys_part_1])

    for i in range(0, 10000):
        round(monkeys_part_2, d)

    monkey_business_part_1 = reduce(operator.mul, sorted(
        [monkey.inspected for monkey in monkeys_part_1])[-2:], 1)
    monkey_business_part_2 = reduce(operator.mul, sorted(
        [monkey.inspected for monkey in monkeys_part_2])[-2:], 1)

    print(f'part 1: {monkey_business_part_1}')
    print(f'part 2: {monkey_business_part_2}')


if __name__ == '__main__':
    main()
