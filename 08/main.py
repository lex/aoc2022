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


def main():
    with open('input.txt') as f:
        lines = f.readlines()
    grid = [list(map(int, line.strip())) for line in lines]

    visible_trees = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            visible_trees += 1 if visible(grid, x, y) else 0

    print(visible_trees)


if __name__ == '__main__':
    main()
