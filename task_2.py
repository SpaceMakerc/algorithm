#По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = int(input('Введите число x: '))
y1 = int(input('Введите число y: '))


y = 'y'
if -x1 > 0:
    print(f'y=k{-x1}+kx+{y1}')
else:
    print(f'y=-k{x1}+kx+{y1}')
