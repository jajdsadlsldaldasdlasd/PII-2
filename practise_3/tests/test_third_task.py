import pytest
from tasks.third_task import print_pack_report


def test_print_pack_report_output(capsys):
    """Проверяет корректность вывода отчета для диапазона чисел от 6 до 1."""
    print_pack_report(6)
    captured = capsys.readouterr()
    output = captured.out

    assert "6" in output
    assert "расфасуем по 3" in output
    assert "5" in output
    assert "расфасуем по 5" in output
    assert "4" in output
    assert "не заказываем!" in output


def test_multiple_of_15_output(capsys):
    """Проверяет вывод специального правила для чисел, кратных 3 и 5 одновременно."""
    print_pack_report(15)
    captured = capsys.readouterr()
    assert "расфасуем по 3 или по 5" in captured.out
