"""Testing solution.py file with."""
from solution import students_study, lottery, fruit_order


def test_coffee_1():
    """Should return True on all occasions."""
    for i in range(18, 25):
        assert students_study(i, True) is True


def test_coffee_2():
    """Should return True on all occasions."""
    for i in range(18, 25):
        assert students_study(i, False) is True


def test_coffee_3():
    """Should return False, since its daytime, but coffee is False."""
    for i in range(5, 18):
        assert students_study(i, False) is False


def test_coffee_4():
    """Should return True, since its daytime and coffee is True."""
    for i in range(5, 18):
        assert students_study(i, True) is True


def test_coffee_5():
    """Should return False on all occasions."""
    for i in range(1, 5):
        assert students_study(i, True) is False


def test_coffee_6():
    """Should return False on all occasions."""
    for i in range(1, 5):
        assert students_study(i, False) is False


def test_lottery_1():
    """Should return 10, since all of the numbers are 5."""
    assert lottery(5, 5, 5) == 10


def test_lottery_2():
    """Should return 5, since all of the numbers are equal, but not 5."""
    assert lottery(4, 4, 4) == lottery(-5, -5, -5) == lottery(0, 0, 0) == 5


def test_lottery_3():
    """Should return 1, since both b and c are different from a."""
    assert lottery(1, 2, 3) == lottery(-1, -2, -3) == lottery(1, 2, 2) == lottery(-1, -2, -2) == 1


def test_lottery_4():
    """Should return 0, since either b or c is equal to a."""
    assert lottery(1, 1, 3) == lottery(-1, -1, -3) == lottery(1, 3, 1) == lottery(-1, -3, -1) == lottery(0, 0, 1) == 0


def test_fruits_1():
    """Should return 1."""
    assert fruit_order(1, 1, 1) == fruit_order(1, 1, 6) == fruit_order(3, 1, 6) == 1


def test_fruits_2():
    """Should return 5."""
    assert fruit_order(5, 1, 10) == 5


def test_fruits_3():
    """Should return 0."""
    assert fruit_order(0, 0, 0) == fruit_order(10, 10, 0) == fruit_order(10, 10, 10) == 0


def test_fruits_4():
    """Should return -1."""
    assert fruit_order(3, 3, 9) == -1
    assert fruit_order(3, 3, 25) == -1
    assert fruit_order(0, 1, 10) == -1
    assert fruit_order(7, 4, 28) == -1


def test_fruits_5():
    """Zeroes."""
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(0, 0, 1) == -1
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(0, 1, 1) == -1
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(1, 0, 1) == 1
    assert fruit_order(1, 1, 0) == 0
    assert fruit_order(1, 1, 1) == 1
    assert fruit_order(1, 0, 9) == -1
    assert fruit_order(0, 1, 9) == -1
    assert fruit_order(0, 10, 10) == 0
    assert fruit_order(10, 0, 9) == 9


def test_fruits_6():
    """Big numbers."""
    assert fruit_order(105, 105, 630) == 105
    assert fruit_order(0, 105, 600) == -1
    assert fruit_order(105, 0, 600) == -1
    assert fruit_order(105, 200, 700) == 0
    assert fruit_order(105, 105, 700) == -1
    assert fruit_order(120, 120, 400) == 0
    assert fruit_order(120, 120, 124) == 4
    assert fruit_order(1, 120, 302) == -1
