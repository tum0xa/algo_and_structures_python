# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input("Type value of X of a first point: "))
y1 = int(input("Type value of Y of a first point "))

x2 = int(input("Type value of X of a second point: "))
y2 = int(input("Type value of Y of a second point "))

k = (y2 - y1) / (x2 - x1)
b = (x2 * y1 - x1 * y2) / (x2 - x1)

if k == 1:
    k = ''
elif k == -1:
    k = '-'
else:
    k = f'{k}*'

if b < 0:
    b = f'- {abs(b)}'
else:
    b = f'+ {b}'

print(f"Your function is Y = {k}X {b}")
