import string

with open('input.txt') as f:
    lines = f.readlines()

sum_of_priorities_part_1 = 0
sum_of_priorities_part_2 = 0

for line in lines:
    line = line.strip()
    first_half, second_half = (line[:len(line) // 2], line[len(line) // 2:])
    for c in string.ascii_letters:
        if c in first_half and c in second_half:
            sum_of_priorities_part_1 += string.ascii_letters.index(c) + 1

print(f'part 1: {sum_of_priorities_part_1}')

for group in [lines[i:i + 3] for i in range(0, len(lines), 3)]:
    r1 = group[0].strip()
    r2 = group[1].strip()
    r3 = group[2].strip()
    for c in string.ascii_letters:
        if c in r1 and c in r2 and c in r3:
            sum_of_priorities_part_2 += string.ascii_letters.index(c) + 1

print(f'part 2: {sum_of_priorities_part_2}')
