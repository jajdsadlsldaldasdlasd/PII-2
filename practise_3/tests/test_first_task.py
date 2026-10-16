import pytest
from tasks.first_task import caesar_cipher, detect_lang


def test_detect_lang_russian():
    """Проверяет определение русского алфавита по входной строке."""
    lower, upper = detect_lang("Привет")
    assert "а" in lower
    assert "Я" in upper


def test_detect_lang_english():
    """Проверяет определение английского алфавита по входной строке."""
    lower, upper = detect_lang("Hello")
    assert "a" in lower
    assert "Z" in upper


def test_caesar_encrypt_english():
    """Проверяет корректность шифрования английского текста со сдвигом 3."""
    result = caesar_cipher("abc", shift=3, mode="encrypt")
    assert result == "def"


def test_caesar_decrypt_english():
    """Проверяет корректность дешифрования английского текста со сдвигом 3."""
    result = caesar_cipher("def", shift=3, mode="decrypt")
    assert result == "abc"


def test_caesar_encrypt_russian():
    """Проверяет корректность шифрования русского текста со сдвигом 1."""
    result = caesar_cipher("абв", shift=1, mode="encrypt")
    assert result == "бвг"


def test_caesar_preserves_case_and_symbols():
    """Проверяет сохранение регистра букв, пробелов и знаков пунктуации."""
    result = caesar_cipher("Hello, World!", shift=1, mode="encrypt")
    assert result == "Ifmmp, Xpsme!"
