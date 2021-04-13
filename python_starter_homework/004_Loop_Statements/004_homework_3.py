a = int(input('Enter numbers: '))
b = int(input('Enter numbers: '))
sum_natural = 0
if a > b:
    print('a < b')
else:
    for i in range(a, b+1):
        sum_natural += i
    print(sum_natural)
