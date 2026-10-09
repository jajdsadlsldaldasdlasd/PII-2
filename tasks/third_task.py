def print_pack_report(start_number):
    """
    Выводит отчёт о том, как расфасовать пирожные по коробкам.

    Перебирает числа от start_number до 1 в порядке убывания
    и для каждого выводит, можно ли его расфасовать по 3, по 5,
    по 3 и 5 одновременно, или нельзя расфасовать вообще.

    Args:
        start_number (int): Положительное целое число больше 1.

    Returns:
        None: Функция ничего не возвращает, только печатает отчёт.

    Example:
        >>> print_pack_report(6)
        6 - расфасуем по 3
        5 - расфасуем по 5
        4 - не заказываем!
        3 - расфасуем по 3
        2 - не заказываем!
        1 - не заказываем!
    """
    for number in range(start_number, 0, -1):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} - расфасуем по 3 или по 5")
        elif number % 5 == 0:
            print(f"{number} - расфасуем по 5")
        elif number % 3 == 0:
            print(f"{number} - расфасуем по 3")
        else:
            print(f"{number} - не заказываем!")


if __name__ == "__main__":
    cupcakes_amount = int(input("Введите число больше 1: "))
    print_pack_report(cupcakes_amount)