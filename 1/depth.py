from numpy import sum
measurements = []
with open('input.txt', 'r') as f:
    measurement = f.read()
    measurements = measurement.split('\n')

measurements = [int(m) for m in measurements]
# print(measurements)
part_one_result = 0
prev_m = measurements[0]

for m in measurements:
    if m > prev_m and prev_m != None:
        part_one_result += 1
    prev_m = m
print(part_one_result)

# part 2

part_two_result = 0
prev_three_measurements = sum(measurements[:3])
print(prev_three_measurements)
print(len(measurements))
for i in range(3, len(measurements), 1):
    try:
        curr_sum = sum(measurements[i - 2 : i + 1])
        if curr_sum > prev_three_measurements:
            part_two_result += 1
        prev_three_measurements = curr_sum
    except:
        print(i)
        print(measurements[i])
        break
print(part_two_result)