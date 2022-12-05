import re
import copy

with open('input.txt') as f:
    lines = f.readlines()

stacks_reversed = False
stacks = []
stacks_part_two = []

for line in lines:
    if '[' in line:
        stack = 1
        i = 1

        while True:
            try:
                if len(stacks) - 1 < stack:
                    stacks.append([])

                v = line[i]

                if v != ' ':
                    stacks[stack - 1].append(v)
            except:
                break
            stack += 1
            i += 4

    if not 'move' in line:
        continue

    if not stacks_reversed:
        for stack in stacks:
            stack.reverse()
        stacks_reversed = True
        stacks_part_two = copy.deepcopy(stacks)

    count, stack_source, stack_destination = [
        int(s) - 1 for s in re.findall(r'\d+', line)]

    temp_stack = []

    for i in range(0, count + 1):
        v = stacks[stack_source].pop()
        stacks[stack_destination].append(v)
        vv = stacks_part_two[stack_source].pop()
        temp_stack.append(vv)

    for v in reversed(temp_stack):
        stacks_part_two[stack_destination].append(v)


top_crates_part_one = ''.join(
    map(lambda x: x[-1] if len(x) > 0 else '', stacks))
top_crates_part_two = ''.join(
    map(lambda x: x[-1] if len(x) > 0 else '', stacks_part_two))
print(f'part 1: {top_crates_part_one}')
print(f'part 2: {top_crates_part_two}')
