n = abs(int(input('Enter numerical value: ')))

stairs = [1, 1]
sum_last_values = 0

for i in range(n - 2):
    stairs.append(stairs[i] + stairs[i + 1])
    sum_last_values = stairs[-1] + stairs[-2]
print(sum_last_values)