import numpy as np

with open('input.txt', 'r') as f:
    datas = f.read()

datas = datas.split('\n')
# print(datas)

# part one

gamma_rate = ''
epsilon_rate = ''
print(datas)
print(len(datas))

data_len = len(datas[0])
for i in range(data_len):
    common = 0
    number_of_ones = 0
    number_of_zeros = 0
    for data in datas:
        #print(data[i])
        if data[i] == '0':
            common -= 1
            number_of_zeros += 1
        else:
            common += 1
            number_of_ones += 1
    print(f'{number_of_ones} > {number_of_zeros}')
    if number_of_ones > number_of_zeros:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
print(len(epsilon_rate) == data_len)

print(gamma_rate)
print(epsilon_rate)

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
