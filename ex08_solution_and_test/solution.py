"""Solution and test."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 0 < time < 25:
        if time in range(5, 18) and coffee_needed is True:
            return True
        elif time in range(18, 25):
            return True
        else:
            return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c:
        return 1
    elif a == b or a == c:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if small_baskets + big_baskets * 5 >= ordered_amount:
        if ordered_amount / 5 > big_baskets:
            if ordered_amount % 5 > small_baskets:
                return -1
            elif ordered_amount % 5 <= small_baskets:
                return ordered_amount - big_baskets * 5
        elif ordered_amount / 5 <= big_baskets:
            if ordered_amount % 5 > small_baskets:
                return -1
            elif ordered_amount % 5 <= small_baskets:
                return ordered_amount % 5
    else:
        return -1


if __name__ == '__main__':
    # print(students_study(0, False))
    # print(lottery(5, -5, -5))
    print(fruit_order(105, 105, 630))
