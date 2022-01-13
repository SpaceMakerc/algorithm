# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака.
a = 5
b = 6
first = a & b
second = a|b
third = a^b
fourth_1 = ~a
fourth_2 = ~b
fifth = a<<2
sixth = a>>2
print(f'{fifth}\n{second}\n{third}\n{fourth_1}\n{fourth_2}\n{fifth}\n{sixth}')
