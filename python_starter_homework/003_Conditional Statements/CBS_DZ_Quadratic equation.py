a = float(input('Enter numbers a: '))
b = float(input('Enter numbers b: '))
c = float(input('Enter numbers c: '))
d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print('D={} root x1={} x2={}'.format(d, x1, x2))
elif d == 0:
    x1 = -b/(-2*a)
    print('D = {} root {}'.format(d, x1))
else:
    print('No root')