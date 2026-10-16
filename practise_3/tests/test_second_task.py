import pytest
from tasks.second_task import check_winners


def test_student_in_top_three():
    """Проверяет попадание участника в тройку лидеров при достаточном балле."""
    scores = [10, 20, 30, 40, 50]
    assert check_winners(scores, 40) is True


def test_student_not_in_top_three():
    """Проверяет случай, когда балл участника ниже проходного в топ-3."""
    scores = [10, 20, 30, 40, 50]
    assert check_winners(scores, 20) is False


def test_student_has_highest_score():
    """Проверяет попадание в топ-3 участника с максимальным баллом."""
    scores = [15, 25, 35, 45]
    assert check_winners(scores, 45) is True
