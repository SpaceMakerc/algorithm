# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
print('Введите три числа')
a = int(input('Введите первое число (a): '))
b = int(input('Введите второе число (b): '))
c = int(input('Введите третье число (c): '))

if b < a:
    if a < c:
        print('a - среднее')
    elif b < c:
        print('с - среднее')
    else:
        print('b - среднее')
elif c < a:
    print('a - среднее')
elif c < b:
    print('с - среднее')
else:
    print('b - среднее')
