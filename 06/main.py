with open('input.txt') as f:
    lines = f.readlines()

signal = lines[0]

for i in range(0, len(signal) - 4):
    l = signal[i:i+4]
    s = set(l)

    if len(l) == len(s):
        print(f'part 1: {i+4}')
        break

for i in range(0, len(signal) - 14):
    l = signal[i:i+14]
    s = set(l)

    if len(l) == len(s):
        print(f'part 2: {i+14}')
        break
