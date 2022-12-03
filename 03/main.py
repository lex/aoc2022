import string

with open('input.txt') as f:
    lines = f.readlines()

sum_of_priorities = 0

for line in lines:
    line = line.strip()
    first_half, second_half = (line[:len(line) // 2], line[len(line) // 2:])
    for c in string.ascii_letters:
        if c in first_half and c in second_half:
            sum_of_priorities += string.ascii_letters.index(c) + 1

print(sum_of_priorities)
