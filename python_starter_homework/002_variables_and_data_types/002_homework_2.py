a = int(input('Enter numbers: '))
b = int(input('Enter numbers: '))
x = int(input('Enter numbers: '))
# Решение используя ветвление
if a < b:  # ожидаем что переменная 'a' это начало диапазона, а 'b' конец диапазона
    print(a < x < b)
else:  # обрабатываем иной сценарий когда переменная 'b' начало, а переменная 'a' конец
    print(a > x > b)
# решение используя операторы сравнения
print(a < b > x or a > b < x)
