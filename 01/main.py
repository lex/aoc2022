lines = None

with open('input.txt') as f:
    lines = f.readlines()

calories = []
current = 0

for line in lines:
    line = line.strip()

    if not line:
        calories.append(current)
        current = 0
        continue

    current += int(line)

calories.sort()
print(sum(calories[-3:]))
