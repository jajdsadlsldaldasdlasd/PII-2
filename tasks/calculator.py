import numpy as np

a = float(input("Первое число: "))
b = float(input("Второе число: "))
if not str(a).replace('.', '', 1).isdigit() or not str(b).replace('.', '', 1).isdigit():
    print("Ошибка: нужно вводить числа")
print('Введите "exit" для выхода')
op = input("Выберите действие (+, -, *, /, ^): ")

while True:
    if op == 'exit':
        break
    else:
        if op == '+':
            print(f'{a} + {b} = {np.add(a, b)}')
            break
        elif op == '-':
            print(f'{a} - {b} = {np.subtract(a, b)}')
        elif op == '*':
            print(f'{a}*{b} = {np.multiply(a, b)}')
        elif op == '/':
            print(f'{a} / {b} = {np.divide(a, b)}')
        elif op == '^':
                print(f'{a} ^ {b} = {np.float_power(a,b)}')
        else:
            print("Неизвестное действие")
            break
