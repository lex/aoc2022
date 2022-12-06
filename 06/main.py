with open('input.txt') as f:
    lines = f.readlines()

signal = lines[0]

for part in [1, 2]:
    f = 4 if part == 1 else 14

    for i in range(0, len(signal) - f):
        l = signal[i:i+f]
        s = set(l)

        if len(l) == len(s):
            print(f'part {part}: {i+f}')
            break
