stairs_value = int(input('Enter stairs number: '))

stairs_list = [1, 1]


def stairs(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return stairs(n-1) + stairs(n-2)


print(stairs(stairs_value))
print(stairs_list)
print(len(stairs_list))
