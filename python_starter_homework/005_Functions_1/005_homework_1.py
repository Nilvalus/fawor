def arif(numbers):
    if numbers < 0:
        return numbers * 1
    else:
        return numbers * 2


def main():
    five = -5
    while five < 5:
        y = arif(five)
        five += 0.5
        print('function(', five, ')=', y, sep='')


if __name__ == '__main__':
    main()
