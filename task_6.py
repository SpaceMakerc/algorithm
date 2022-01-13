# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из
# этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.
print('Введите три отрезка')
a = int(input('Введите первый отрезок:'))
b = int(input('Введите второй отрезок:'))
c = int(input('Введите третий отрезок:'))

if a + b > c:
    if b + c > a:
        if a + c > b:
            if a!= 0 and b!= 0 and c!=0:
                print('Есть возможность построить треугольник')
else:
    print('Нет возможности построить треугольник')
if a!= b and b!= c and c!= a:
    print('Треугольник разносторонний')
elif a == b and b == c and c == a:
    print('Треугольник равносторонний')
if a == b:
    if a!= c:
        print('Треугольник равнобедренный')
elif b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник не равнобедренный')
