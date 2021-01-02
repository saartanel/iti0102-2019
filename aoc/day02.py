"""AOC day 2."""


def do_big_data(input_txt, a=12, b=2):
    """
    Title.

    :param input_txt:
    :param a:
    :param b:
    :return:
    """
    start = 0
    big_data = input_txt.copy()
    big_data[1] = a
    big_data[2] = b
    while True:
        if big_data[start] == 1:
            big_data[big_data[start + 3]] = big_data[big_data[start + 1]] + big_data[big_data[start + 2]]
        elif big_data[start] == 2:
            big_data[big_data[start + 3]] = big_data[big_data[start + 1]] * big_data[big_data[start + 2]]
        elif big_data[start] == 99:
            break
        start += 4

    return big_data[0]


def do_even_bigger_data(data):
    """
    Title.

    :param data:
    :return:
    """
    for a in range(50):
        for b in range(50):
            if do_big_data(data, a, b) == 19690720:
                return 100 * a + b


if __name__ == '__main__':
    big_data = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 2, 9, 19, 23, 1, 9, 23, 27, 2, 27, 9, 31, 1, 31, 5, 35, 2, 35, 9, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 47, 6, 51, 2, 51, 10, 55, 1, 9, 55, 59, 2, 6, 59, 63, 1, 63, 6, 67, 1, 67, 10, 71, 1, 71, 10, 75, 2, 9, 75, 79, 1, 5, 79, 83, 2, 9, 83, 87, 1, 87, 9, 91, 2, 91, 13, 95, 1, 95, 9, 99, 1, 99, 6, 103, 2, 103, 6, 107, 1, 107, 5, 111, 1, 13, 111, 115, 2, 115, 6, 119, 1, 119, 5, 123, 1, 2, 123, 127, 1, 6, 127, 0, 99, 2, 14, 0, 0]
    print(do_big_data(big_data))
    print(do_even_bigger_data(big_data))
