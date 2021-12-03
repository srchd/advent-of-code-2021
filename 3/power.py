import numpy as np

with open('input.txt', 'r') as f:
    datas = f.read()

datas = datas.split('\n')
# print(datas)

# part one

gamma_rate = ''
epsilon_rate = ''
# print(datas)
# print(len(datas))

data_len = len(datas[0])
for i in range(data_len):
    common = 0
    number_of_ones = 0
    number_of_zeros = 0
    for data in datas:
        # print(data[i])
        if data[i] == '0':
            common -= 1
            number_of_zeros += 1
        else:
            common += 1
            number_of_ones += 1
    # print(f'{number_of_ones} > {number_of_zeros}')
    if number_of_ones > number_of_zeros:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
# print(len(epsilon_rate) == data_len)

# print(gamma_rate)
# print(epsilon_rate)

gamma = int(gamma_rate)
epsilon = int(epsilon_rate)


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


print(f'Part One: {binaryToDecimal(gamma) * binaryToDecimal(epsilon)}')

# part two


def filter_datas(data_type, remaining_data, pos=0):

    if len(remaining_data) == 1:
        return remaining_data[0]

    common = 0
    return_datas = []
    for data in remaining_data:
        if data[pos] == '0':
            common -= 1
        else:
            common += 1
    for data in remaining_data:
        if common > 0:
            if data[pos] == '1' and data_type == 'o':
                return_datas.append(data)
            elif data[pos] == '0' and data_type == 'c':
                return_datas.append(data)
        elif common < 0:
            if data[pos] == '0' and data_type == 'o':
                return_datas.append(data)
            elif data[pos] == '1' and data_type == 'c':
                return_datas.append(data)
        elif common == 0:
            if data_type == 'o':
                if data[pos] == '1':
                    return_datas.append(data)
            elif data_type == 'c':
                if data[pos] == '0':
                    return_datas.append(data)

    return filter_datas(data_type, return_datas, pos + 1)


oxygen = filter_datas('o', datas)
co2 = filter_datas('c', datas)
print(f'Oxygen: {oxygen}')
print(f'CO2: {co2}')

print(f'Part Two: {binaryToDecimal(int(oxygen)) * binaryToDecimal(int(co2))}')