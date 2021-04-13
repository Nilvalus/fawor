a = int(input('Enter modification: '))
b = int(input('Enter value range: '))
new_list = list(range(a, b+1))


def max_min_sum_aver(list):
    max_value = max(list)
    min_value = min(list)
    sum_new_list = sum(list)
    average_new_list = sum_new_list // len(new_list)
    return 'Max=', max_value, 'Min=', min_value, 'Sum=', sum_new_list, 'Average=', average_new_list


print(new_list)
print(max_min_sum_aver(new_list))
