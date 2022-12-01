lines = None

with open('input.txt') as f:
    lines = f.readlines()

most = 0
current = 0

for line in lines:
    line = line.strip()

    if not line:
        if current > most:
            most = current
        current = 0
        continue

    current += int(line)

print(most)
