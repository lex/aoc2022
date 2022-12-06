with open('input.txt') as f:
    lines = f.readlines()

signal = lines[0]

for i in range(0, len(signal) - 4):
    c1, c2, c3, c4 = signal[i:i+4]
    l = [c1, c2, c3, c4]
    s = set(l)

    if len(l) == len(s):
        print(i+4)
        break
