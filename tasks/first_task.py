def detect_lang(text):
    """
    Определяет язык текста (русский или английский).


    Args: 
        text (str): Исходный текст.

    
    Returns:
        tuple (str): Кортеж из двух строк (lower_alphabet, upper_alphabet).

    
    Example:
        >>> detect_lang("Привет")
        ("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
        >>> detect_lang("Hello")
        ("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    """
    for char in text.lower():
        if 'а' <= char <= 'я' or char == 'ё':
            return "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    return "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Шифрует и дешифрует текст шифром Цезаря.
    
    Args:
        text (str): Исходный текст.
        shift (int): Шаг сдвига.
        mode (str): 'encrypt' для шифрования, 'decrypt' для дешифровки.
        
    Returns:
        str: Преобразованный текст.
    """
    # Определяем алфавит
    lower_alphabet, upper_alphabet = detect_lang(text)
    
    # Если дешифруем — просто меняем знак сдвига на противоположный
    if mode == 'decrypt':
        shift = -shift
        
    result = ""
    
    for char in text:
        if char in lower_alphabet:
            # Находим индекс буквы, сдвигаем, берём остаток от деления
            old_index = lower_alphabet.index(char)
            new_index = (old_index + shift) % len(lower_alphabet)
            result += lower_alphabet[new_index]
            
        elif char in upper_alphabet:
            old_index = upper_alphabet.index(char)
            new_index = (old_index + shift) % len(upper_alphabet)
            result += upper_alphabet[new_index]
            
        else:
            # Пробелы, цифры и знаки препинания оставляем без изменений
            result += char
            
    return result

def main():
    """Основная функция для взаимодействия с пользователем."""
    print("Шифр Цезаря")
    print("1 - Зашифровать")
    print("2 - Дешифровать")
    
    choice = input("Выберите действие (1 или 2): ")
    
    if choice not in ('1', '2'):
        print("Ошибка: нужно выбрать 1 или 2")
        return
        
    text = input("Введите текст: ")
    
    try:
        shift = int(input("Введите шаг сдвига (например, 3): "))
    except ValueError:
        print("Ошибка: шаг сдвига должен быть целым числом")
        return
        
    if choice == '1':
        result = caesar_cipher(text, shift, mode='encrypt')
        print(f"\nЗашифрованный текст:\n{result}")
    else:
        result = caesar_cipher(text, shift, mode='decrypt')
        print(f"\nДешифрованный текст:\n{result}")


if __name__ == "__main__":
    main()