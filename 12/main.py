import collections

with open('input.txt') as f:
    lines = f.readlines()


def bfs(graph, start, end):
    shortest = {start: 0}
    q = collections.deque(((start, 0),))

    while q:
        i_current, steps = q.popleft()
        next_steps = steps + 1

        for neighbor in graph[i_current]:
            if neighbor not in shortest or next_steps < shortest[neighbor]:
                shortest[neighbor] = next_steps

                if neighbor != end:
                    q.append((neighbor, next_steps))

    return shortest[end]


def create_neighbors(x, y):
    current = lines[y][x]
    neighbors = []

    # up
    if y != 0:
        up = lines[y-1][x]
        if ord(up) - ord(current) <= 1:
            neighbors.append((y-1, x))

    # down
    if y != len(lines) - 1:
        down = lines[y+1][x]
        if ord(down) - ord(current) <= 1:
            neighbors.append((y+1, x))

    # left
    if x != 0:
        left = lines[y][x - 1]
        if ord(left) - ord(current) <= 1:
            neighbors.append((y, x - 1))

    # right
    if x != len(lines[0]) - 2:
        right = lines[y][x + 1]
        if ord(right) - ord(current) <= 1:
            neighbors.append((y, x + 1))

    return neighbors


def main():
    graph = collections.defaultdict(list)

    start = 0
    end = 0

    for y in range(0, len(lines)):
        for x in range(0, len(lines[0]) - 1):
            c = lines[y][x]

            if c == 'S':
                start = (y, x)
                lines[y] = lines[y].replace('S', 'a')

            if c == 'E':
                end = (y, x)
                lines[y] = lines[y].replace('E', 'z')

    for y in range(0, len(lines)):
        for x in range(0, len(lines[0]) - 1):
            neighbors = create_neighbors(x, y)

            for n in neighbors:
                graph[(y, x)].append(n)

    b = bfs(graph, start, end)
    print(f'part 1: {b}')


if __name__ == '__main__':
    main()
