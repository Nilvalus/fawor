a = int(input('Enter triangle width: '))
b = int(input('Enter triangle height: '))
for i in range(0, a):
    for k in range(0, i+1):
        print('*', end='')
    print()

for w in range(a+1, 0, -1):
    for j in range(0, w -1):
        print('*', end='')
    print()

c = b * a -b
for m in range(a, -1, -1):
    for n in range(c, 0, -1):
        print(end='')
    c += 1
    for n in range(0, m+1):
        print('*', end='')
    print()

