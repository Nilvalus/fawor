import math

x = float(input('Enter value x: '))
result = None
if -math.pi <= x <= math.pi:
    result = math.cos(3*x)
elif x < -math.pi  or x > math.pi:
    result = x
if result is None:
    print(None)

print(result)
