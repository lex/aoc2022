with open('input.txt') as f:
    lines = f.readlines()


class Instruction:
    def __init__(self, operation, cycles_left, argument=None):
        self.operation = operation
        self.cycles_left = cycles_left
        self.argument = argument

    def __str__(self):
        return f'{self.operation} {self.argument} ({self.cycles_left})'


x = 1
cycle = 1
instructions = []
interesting_cycles = [20, 60, 100, 140, 180, 220]
interesting_cycles_signal_strength_sum = 0
crt_frame = ''
crt_row = ''

while True:
    if len(crt_row) == 40:
        crt_frame += f'{crt_row}\n'
        crt_row = ''

    crt_index = len(crt_row)
    crt_row += '#' if crt_index in range(x - 1, x + 2) else '.'

    if not lines and not instructions:
        break

    if cycle in interesting_cycles:
        interesting_cycles_signal_strength_sum += cycle * x

    if not instructions:
        line = lines[0]
        lines = lines[1:]

        instruction = line.strip().split(' ')[0]

        if instruction == 'noop':
            instructions.append(Instruction('noop', 1))
        if instruction == 'addx':
            argument = int(line.strip().split(' ')[1])
            instructions.append(Instruction('addx', 2, argument))

    instruction = instructions[0]
    instruction.cycles_left -= 1

    if instruction.cycles_left == 0:
        if instruction.operation == 'addx':
            x += instruction.argument
        instructions = instructions[1:]
    cycle += 1


print(f'part 1: {interesting_cycles_signal_strength_sum}')
print(f'part 2:\n{crt_frame}')
