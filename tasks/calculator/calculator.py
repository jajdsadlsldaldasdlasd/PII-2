import numpy as np


def add_numbers(a: float, b: float) -> float:
    """
    Складывает два числа.

    Args:
        a (float): Первое слагаемое.
        b (float): Второе слагаемое.

    Returns:
        float: Сумма двух чисел.

    Example:
        >>> add_numbers(2, 3)
        5.0
    """
    return np.add(a, b)


def check(x):
    """
    Проверяет, является ли значение числом.

    Args:
        x (any): Значение для проверки (строка, число и т.д.).

    Returns:
        bool: True, если значение можно привести к числу, иначе False.

    Example:
        >>> check("3.14")
        True
        >>> check("abc")
        False
    """

    return str(x).replace(".", "", 1).isdigit()


if __name__ == "__main__":
    a_input = input("Первое число (если десятичная дробь, то вводите '.'): ")
    b_input = input("Второе число (если десятичная дробь, то вводите '.'): ")

    if not check(a_input) or not check(b_input):
        print("Ошибка: нужно вводить числа")
        exit()

    a = float(a_input)
    b = float(b_input)

    op = input("Выберите действие (+, -, *, /, ^): ")

    if op == "+":
        print(f"{a} + {b} = {add_numbers(a, b)}")
    elif op == "-":
        print(f"{a} - {b} = {np.subtract(a, b)}")
    elif op == "*":
        print(f"{a} * {b} = {np.multiply(a, b)}")
    elif op == "/":
        print(f"{a} / {b} = {np.divide(a, b)}")
    elif op == "^":
        print(f"{a} ^ {b} = {np.float_power(a, b)}")
    else:
        print("Неизвестное действие")