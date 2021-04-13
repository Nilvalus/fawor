def is_name(name='Artem'):
    print('Hello, ', name, '!')


your_name = input('Enter your name: ')
if your_name:
    is_name(your_name)
else:
    is_name()

