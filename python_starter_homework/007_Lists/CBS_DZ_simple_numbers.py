from functools import reduce

simple_numbers = []


def user_enter():
    user = input('Display the sum of found numbers enter 1 else 2 to display the product of the found numbers: ')
    if user == '1':
        print(sum(simple_numbers))
    elif user == '2':
        print(reduce(lambda x, y: x * y, simple_numbers))
    else:
        pass


def numeric(arg_1, arg_2):
    new_list_1 = list(range(arg_1, arg_2))
    for x in new_list_1:
        if x == 1:
            continue
        elif simple(x):
            simple_numbers.append(x)


def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    a = abs(int(input('Enter start range: ')))
    b = abs(int(input('Enter end range: ')))
    numeric(a, b)
    print(simple_numbers)
    user_enter()


if __name__ == '__main__':
    main()
