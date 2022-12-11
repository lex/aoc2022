import operator
import functools

with open('input.txt') as f:
    lines = f.readlines()


class Monkey:
    def __init__(self, number, items, operation, test, throw_true, throw_false):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspected = 0


monkeys = []

for i in range(0, len(lines), 7):
    c = lines[i:i + 7]
    number = int(c[0].split('Monkey ')[1].strip()[:-1])
    starting_items = list(
        map(lambda x: int(x), c[1].split(': ')[1].strip().split(', ')))
    operation = c[2].split(': ')[1].strip()
    test = int(c[3].split(': ')[1].strip().split('divisible by ')[1])
    true = int(c[4].split(': ')[1].strip().split('throw to monkey ')[1])
    false = int(c[5].split(': ')[1].strip().split('throw to monkey ')[1])
    m = Monkey(number, starting_items, operation, test, true, false)
    monkeys.append(m)


for i in range(0, 20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1

            new = 0
            old = item
            exec(monkey.operation)
            new = new // 3

            if new % monkey.test == 0:
                monkeys[monkey.throw_true].items.append(new)
            else:
                monkeys[monkey.throw_false].items.append(new)

        monkey.items = []

monkey_business = functools.reduce(operator.mul, sorted(
    [monkey.inspected for monkey in monkeys])[-2:], 1)

print(f'part 1: {monkey_business}')
