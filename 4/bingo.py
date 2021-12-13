import numpy as np

with open('input.txt', 'r') as file:
    numbers = file.readline()
    numbers = numbers.split(',')

    boards = file.read()
    boards = boards.split('\n\n')

numbers[-1] = numbers[-1].strip('\n')
numbers = [int(num) for num in numbers]

temp_board = []
for board in boards:
    tmp = board.split('\n')
    temp_board.append(tmp)
temp_board[0].pop(0)

final_boards = []
final_board = []
final_row = []

for board in temp_board:
    for row in board:
        tmp = row.split(' ')
        for number in tmp:
            try:
                final_row.append(int(number))
            except ValueError:
                pass
        final_board.append(final_row)
        final_row = []
    final_boards.append(final_board)
    final_board = []

np_board = np.array(final_boards)

# Gross solution, part one:

i_len = len(np_board)
j_len = len(np_board[0])
k_len = len(np_board[0][0])

result = 0
winner_board = 0
for number in numbers:
    for i in range(i_len):
        for j in range(j_len):
            for k in range(k_len):
                if np_board[i][j][k] == number:
                    np_board[i][j][k] = 0
    rows_per_board = np.sum(np_board, axis=2)
    columns_per_board = np.sum(np_board, axis=1)
    possible_rows = np.where(rows_per_board == 0)
    possible_cols = np.where(columns_per_board == 0)
    if len(possible_rows[0]) != 0 and len(possible_rows[1]) != 0:
        winner_board = possible_rows[0][0]
        result = number
        break
    elif len(possible_cols[0]) != 0 and len(possible_cols[1]) != 0:
        winner_board = possible_cols[0][0]
        result = number
        break
    else:
        pass

result *= sum(sum(np_board[winner_board]))

print(f'Part One: {result}')

# part two

np_board = np.array(final_boards)

numberOfBoards = np_board.shape[0]

boardsLeft = [i for i in range(100)]

lastBoard = -1
result = 0
winner_board = 0
for number in numbers:
    for i in range(i_len):
        for j in range(j_len):
            for k in range(k_len):
                if np_board[i][j][k] == number:
                    np_board[i][j][k] = 0
    rows_per_board = np.sum(np_board, axis=2)
    columns_per_board = np.sum(np_board, axis=1)
    possible_rows = np.where(rows_per_board == 0)
    possible_cols = np.where(columns_per_board == 0)
    if len(possible_rows[0]) != 0 and len(possible_rows[1]) != 0:
        if boardsLeft.count(-1) == (numberOfBoards - 1):
            result = number
            break
        else:
            for b in possible_rows[0]:
                boardsLeft[b] = -1

    elif len(possible_cols[0]) != 0 and len(possible_cols[1]) != 0:
        if boardsLeft.count(-1) == (numberOfBoards - 1):
            break
        else:
            for b in possible_cols[0]:
                boardsLeft[b] = -1
    else:
        pass

print(boardsLeft)

for b in boardsLeft:
    if b != -1:
        lastBoard = b

print(np_board[b])

result *= sum(sum(np_board[lastBoard]))

print(f'Part Two:{result}')
