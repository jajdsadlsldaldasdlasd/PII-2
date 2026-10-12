import random
import string


def get_settings():
    """
    Запрашивает у пользователя настройки генерации пароля.

    Спрашивает, какие категории символов использовать (строчные буквы,
    заглавные буквы, цифры, спецсимволы), а также длину пароля.
    Возвращает словарь с настройками.

    Args:
        Нет.

    Returns:
        dict: Словарь с настройками генерации пароля следующего вида:
            {
                "lower": bool,   # использовать строчные буквы
                "upper": bool,   # использовать заглавные буквы
                "digits": bool,  # использовать цифры
                "symbols": bool, # использовать спецсимволы
                "length": int,   # длина пароля
            }

    Example:
        >>> get_settings()
        Использовать строчные буквы? (да/нет): да
        ...
        {'lower': True, 'upper': True, 'digits': False, 'symbols': True, 'length': 12}
    """
    print("===> Генератор паролей 3000 <===")
    lower_alph_use = (
        input("Использовать строчные буквы? (да/нет): ").strip().lower() == "да"
    )
    upper_alph_use = (
        input("Использовать заглавные буквы? (да/нет): ").strip().lower() == "да"
    )
    digits_use = input("Использовать цифры? (да/нет): ").strip().lower() == "да"
    spec_symbols_use = (
        input("Использовать специальные символы? (да/нет): ").strip().lower() == "да"
    )
    password_length = int(input("Длина пароля: "))
    return {
        "lower": lower_alph_use,
        "upper": upper_alph_use,
        "digits": digits_use,
        "symbols": spec_symbols_use,
        "length": password_length,
    }


def generate_password(settings: dict) -> str:
    """Генерирует случайный пароль на основе переданных настроек.

    Формирует пул допустимых символов из выбранных категорий (строчные,
    заглавные буквы, цифры, специальные знаки) и создает строку заданной длины.

    Args:
        settings (dict): Словарь с параметрами генерации следующего вида:
            {
                "lower": bool,    # использовать строчные буквы
                "upper": bool,    # использовать заглавные буквы
                "digits": bool,   # использовать цифры
                "symbols": bool,  # использовать спецсимволы
                "length": int,    # итоговая длина пароля
            }

    Returns:
        str: Сгенерированная строка пароля.

    Raises:
        ValueError: Если не выбрана ни одна категория символов или
            если указана длина пароля меньше или равная 0.

    Example:
        >>> options = {
        ...     "lower": True,
        ...     "upper": True,
        ...     "digits": True,
        ...     "symbols": False,
        ...     "length": 8,
        ... }
        >>> pwd = generate_password(options)
        >>> len(pwd)
        8
    """
    chars = ""
    if settings["lower"]:
        chars += string.ascii_lowercase
    if settings["upper"]:
        chars += string.ascii_uppercase
    if settings["digits"]:
        chars += string.digits
    if settings["symbols"]:
        chars += string.punctuation
    if settings["length"] <= 0:
        raise ValueError("Длина пароля должна быть больше нуля")
    if len(chars) == 0:
        raise ValueError("Не выбрана ни одна категория символов")
    selected_chars = random.choices(chars, k=settings["length"])
    password = "".join(selected_chars)
    return password


def main() -> None:
    """Точка входа в программу-генератор паролей.

    Запрашивает у пользователя критерии для генерации пароля через консоль,
    вызывает функцию формирования пароля, обрабатывает возможные ошибки
    ввода и выводит итоговый результат в терминал.

    Args:
        None.

    Returns:
        None.

    Example:
        >>> main()
        ===> Генератор паролей 3000 <===
        ...
    """
    settings = get_settings()

    try:
        password = generate_password(settings)
        print("\n" + "=" * 32)
        print(f"Ваш сгенерированный пароль: {password}")
        print("=" * 32)
    except ValueError as error:
        print(f"\n[Ошибка] Не удалось сгенерировать пароль: {error}")


if __name__ == "__main__":
    main()
