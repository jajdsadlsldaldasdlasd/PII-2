import pytest
from tasks.fourth_task import generate_password


def test_password_exact_length():
    """Проверяет соответствие длины сгенерированного пароля заданному значению."""
    settings = {
        "lower": True,
        "upper": False,
        "digits": False,
        "symbols": False,
        "length": 16,
    }
    password = generate_password(settings)
    assert len(password) == 16


def test_password_only_digits():
    """Проверяет, что при выборе только цифр пароль состоит исключительно из них."""
    settings = {
        "lower": False,
        "upper": False,
        "digits": True,
        "symbols": False,
        "length": 8,
    }
    password = generate_password(settings)
    assert password.isdigit()


def test_password_invalid_length_raises_error():
    """Проверяет выброс исключения ValueError при неположительной длине пароля."""
    settings = {
        "lower": True,
        "upper": True,
        "digits": False,
        "symbols": False,
        "length": 0,
    }
    with pytest.raises(ValueError):
        generate_password(settings)


def test_no_selected_categories_raises_error():
    """Проверяет выброс исключения ValueError, если не выбрана ни одна категория символов."""
    settings = {
        "lower": False,
        "upper": False,
        "digits": False,
        "symbols": False,
        "length": 10,
    }
    with pytest.raises(ValueError):
        generate_password(settings)
