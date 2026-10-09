from calculator import add_numbers


def test_add_positive_numbers():
    """Проверяет сложение двух положительных чисел."""
    assert add_numbers(2, 3) == 5


def test_add_negative_numbers():
    """Проверяет сложение двух отрицательных чисел."""
    assert add_numbers(-1, -2) == -3


def test_add_with_zero():
    """Проверяет сложение с нулём."""
    assert add_numbers(5, 0) == 5


def test_add_floats():
    """Проверяет сложение дробных чисел."""
    assert add_numbers(1.5, 2.5) == 4.0
    