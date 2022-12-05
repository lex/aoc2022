import re

with open('input.txt') as f:
    lines = f.readlines()

stacks_reversed = False
stacks = []

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

    count, stack_source, stack_destination = [
        int(s) - 1 for s in re.findall(r'\d+', line)]

    for i in range(0, count + 1):
        v = stacks[stack_source].pop()
        stacks[stack_destination].append(v)


s = ''.join(map(lambda x: x[-1] if len(x) > 0 else '', stacks))
print(s)
