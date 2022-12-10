with open('input.txt') as f:
    lines = f.readlines()


class RopePart:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rope:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


head = RopePart(0, 0)
tail = RopePart(0, 0)
rope = Rope(head, tail)

tail_positions = {}

for line in lines:
    direction, amount = line.strip().split(' ')
    amount = int(amount)

    print(f'moving {amount} steps to {direction}')
    for i in range(0, amount):
        if direction == 'U':
            # up
            rope.head.y += 1
        elif direction == 'D':
            # down
            rope.head.y -= 1
        elif direction == 'L':
            # left
            rope.head.x -= 1
        elif direction == 'R':
            # right
            rope.head.x += 1

        # move tail if d > 2
        dx = rope.head.x - rope.tail.x
        dy = rope.head.y - rope.tail.y

        if dx > 1:
            rope.tail.x += 1
            rope.tail.y = rope.head.y
        elif dx < -1:
            rope.tail.x -= 1
            rope.tail.y = rope.head.y
        elif dy > 1:
            rope.tail.y += 1
            rope.tail.x = rope.head.x
        elif dy < -1:
            rope.tail.y -= 1
            rope.tail.x = rope.head.x

        tail_positions[(rope.tail.x, rope.tail.y)] = 1

print(len(tail_positions))
