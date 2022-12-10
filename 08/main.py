def visible(grid, x, y):
    # edges
    if x == 0 or y == 0 or x == len(grid) - 1 or x == len(grid[0]) - 1:
        return True

    tree = grid[y][x]

    # up
    if all(row[x] < tree for row in grid[0:y]):
        return True

    # down
    if all(row[x] < tree for row in grid[y+1:]):
        return True

    # left
    if all(t < tree for t in grid[y][0:x]):
        return True

    # right
    if all(t < tree for t in grid[y][x+1:]):
        return True

    return False


def scenic_score(grid, x, y):
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid) - 1:
        return 0

    tree = grid[y][x]

    # up
    for i in range(1, y + 1):
        if grid[y - i][x] >= tree:
            break
    up = i

    # down
    for i in range(1, len(grid) - y):
        if grid[y + i][x] >= tree:
            break
    down = i

    # left
    for i in range(1, x + 1):
        if grid[y][x - i] >= tree:
            break
    left = i

    # right
    right = 0
    for i in range(1, len(grid[0]) - x):
        if grid[y][x + i] >= tree:
            break
    right = i

    return left * right * up * down


def main():
    with open('input.txt') as f:
        lines = f.readlines()
    grid = [list(map(int, line.strip())) for line in lines]

    visible_trees = 0
    highest_scenic_score = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            visible_trees += 1 if visible(grid, x, y) else 0
            score = scenic_score(grid, x, y)
            highest_scenic_score = max(score, highest_scenic_score)

    print(f'part 1: {visible_trees}')
    print(f'part 2: {highest_scenic_score}')


if __name__ == '__main__':
    main()
