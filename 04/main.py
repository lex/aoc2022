with open('input.txt') as f:
    lines = f.readlines()

pairs = 0
total_overlaps = 0

for line in lines:
    first_group, second_group = line.strip().split(',')

    start_first, end_first = first_group.split('-')
    start_second, end_second = second_group.split('-')

    range_first = range(int(start_first), int(end_first) + 1)
    range_second = range(int(start_second), int(end_second) + 1)
    list_first = list(range_first)
    list_second = list(range_second)

    if all(i in list_second for i in list_first) or all(i in list_first for i in list_second):
        pairs += 1

    if any(i in list_second for i in list_first) or any(i in list_first for i in list_second):
        total_overlaps += 1

print(f'part 1: {pairs}')
print(f'part 2: {total_overlaps}')
