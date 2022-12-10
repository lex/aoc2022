with open('input.txt') as f:
    lines = f.readlines()


class Knot:
    def __init__(self, x, y, next_part=None):
        self.x = x
        self.y = y
        self.next_part = next_part
        self.positions = {}

    def pull_next(self):
        if not self.next_part:
            return

        dx = self.x - self.next_part.x
        dy = self.y - self.next_part.y

        if dx > 1:
            self.next_part.x += 1
            self.next_part.y = self.y
        elif dx < -1:
            self.next_part.x -= 1
            self.next_part.y = self.y
        elif dy > 1:
            self.next_part.y += 1
            self.next_part.x = self.x
        elif dy < -1:
            self.next_part.y -= 1
            self.next_part.x = self.x

        self.next_part.pull_next()
        self.next_part.update_positions()

    def update_positions(self):
        self.positions[(self.x, self.y)] = 1


part_1_tail = Knot(0, 0)
part_1_head = Knot(0, 0, part_1_tail)

knots = []
for i in range(0, 10):
    knots.append(Knot(0, 0, knots[-1] if len(knots) else None))

part_2_head = knots[-1]
part_2_tail = knots[0]

heads = [part_1_head, part_2_head]
tails = [part_1_tail, part_2_tail]

for line in lines:
    direction, amount = line.strip().split(' ')
    amount = int(amount)

    for i in range(0, amount):
        if direction == 'U':
            # up
            for head in heads:
                head.y += 1
        elif direction == 'D':
            # down
            for head in heads:
                head.y -= 1
        elif direction == 'L':
            # left
            for head in heads:
                head.x -= 1
        elif direction == 'R':
            # right
            for head in heads:
                head.x += 1

        for head in heads:
            head.pull_next()


for part in [1, 2]:
    print(f'part {part}: {len(tails[part - 1].positions)}')
