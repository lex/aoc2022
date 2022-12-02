lines = None

with open('input.txt') as f:
    lines = f.readlines()

lost = 0
draw = 3
win = 6

outcomes = {
    'A': {
        'X': draw + 1,
        'Y': win + 2,
        'Z': lost + 3,
    },
    'B': {
        'X': lost + 1,
        'Y': draw + 2,
        'Z': win + 3,
    },
    'C': {
        'X': win + 1,
        'Y': lost + 2,
        'Z': draw + 3,
    }
}

total_score = 0

for line in lines:
    split = line.strip().split(' ')
    opponent = split[0]
    my = split[1]
    total_score += outcomes[opponent][my]

print(total_score)
