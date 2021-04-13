print('''To perform the operation, enter
1 - addition;
2 - subtraction;
3 - multiplication;
4 - division;
to exit, enter something else
''')


def addition():
    terms_1 = int(input('Enter terms: '))
    terms_2 = int(input('Enter terms: '))
    print(terms_1 + terms_2)


def subtraction():
    minuend = int(input('Enter minuend: '))
    subtrahend = int(input('Enter subtrahend: '))
    print(minuend - subtrahend)


def multiplication():
    multiplicand = int(input(' Enter multiplicand: '))
    factor = int(input('Enter factor: '))
    print(multiplicand * factor)


def division():
    dividend = int(input('Enter dividend: '))
    divider = int(input('Enter divider: '))
    if dividend != 0 and divider != 0:
        print(dividend / divider)
    else:
        print('Error division zero')


while True:
    operation = input('Enter operation mode: ')
    if operation == '1':
        addition()
    elif operation == '2':
        subtraction()
    elif operation == '3':
        multiplication()
    elif operation == '4':
        division()
    else:
        break
