# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.
import random

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
result = random.randint(a,b)
a1 = int(input('Введите первое число: '))
b1 = int(input('Введите второе число: '))
result_2 = random.uniform(a1, b1)
a2 = (input('Введите первый символ: '))
b2 = (input('Введите второй символ: '))
content = 'abcdefghijklmnopqrstuvwxyz'
x = content.index(a2)
y = content.index(b2)
helper = content[x:y]
helper1 = random.randint(0, len(helper)-1)
result2 = helper[helper1]
print(f'Первое задание - {result},второе задание - {result_2},третье задание - {result2}')
