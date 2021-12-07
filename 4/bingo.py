import numpy as np
from copy import deepcopy

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

print(result)