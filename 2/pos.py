
depth = 0
hor_pos = 0

with open('input.txt', 'r') as f:
    datas = f.read()

datas = datas.split('\n')

# part one
for data in datas:
    command, value = data.split(' ')
    # print(f'{command} value: {value}')
    if command == 'forward':
        hor_pos += int(value)
    elif command == 'up':
        depth -= int(value)
    elif command == 'down':
        depth += int(value)

print(f'Part One: {depth * hor_pos}')

# part two
depth = 0
hor_pos = 0
aim = 0

for data in datas:
    command, value = data.split(' ')
    # print(f'{command} value: {value}')
    if command == 'forward':
        hor_pos += int(value)
        depth += aim * int(value)
    elif command == 'up':
        aim -= int(value)
    elif command == 'down':
        aim += int(value)

print(f'Part Two: {hor_pos * depth}')