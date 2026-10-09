import numpy as np

def check(x):
    return str(x).replace(".", "", 1).isdigit()

a = float(input("Первое число: "))
b = float(input("Второе число: "))

if not check(a) or not check(b):  
    print("Ошибка: нужно вводить числа")

print("""Введите "exit" для выхода""")

op = input("Выберите действие (+, -, *, /, ^): ")

while True:
    if op == "exit":
        break
    else:
        if op == "+":
            print(f"{a} + {b} = {np.add(a, b)}")
            break
        elif op == "-":
            print(f"{a} - {b} = {np.subtract(a, b)}")
            break
        elif op == "*":
            print(f"{a}*{b} = {np.multiply(a, b)}")
            break
        elif op == "/":
            print(f"{a} / {b} = {np.divide(a, b)}")
            break
        elif op == "^":
            print(f"{a} ^ {b} = {np.float_power(a,b)}")
            break
        else:
            print("Неизвестное действие")
            break
