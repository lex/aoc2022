lines = None

with open('input.txt') as f:
    lines = f.readlines()

lost = 0
draw = 3
win = 6

outcomes = {
    'A': {
        'X': (draw, 1),
        'Y': (win, 2),
        'Z': (lost,  3),
    },
    'B': {
        'X': (lost, 1),
        'Y': (draw, 2),
        'Z': (win, 3),
    },
    'C': {
        'X': (win, 1),
        'Y': (lost, 2),
        'Z': (draw, 3),
    }
}

wanted_outcomes = {
    'X': lost,
    'Y': draw,
    'Z': win,
}

total_score_part_1 = 0
total_score_part_2 = 0

for line in lines:
    # part 1
    opponent, my = line.strip().split(' ')
    outcome_part_1 = outcomes[opponent][my]
    total_score_part_1 += outcome_part_1[0] + outcome_part_1[1]

    # part 2
    candidates = list(outcomes[opponent].items())
    outcome_part_2 = list(
        filter(lambda x: x[1][0] == wanted_outcomes[my], candidates))[0]

    total_score_part_2 += outcome_part_2[1][0] + outcome_part_2[1][1]

print(f'part 1: {total_score_part_1}')
print(f'part 2: {total_score_part_2}')
