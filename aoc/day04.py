"""AOC day 4."""


def part1():
    """
    Smaller data.
    :return:
    """
    a = []
    for i in range(246540, 787419 + 1):
        nr = list(str(i))
        if nr != sorted(nr) or len(set(nr)) == len(nr):
            pass
        else:
            a.append(nr)
    return a


def part2(a):
    """
    Abit bigger data.
    :param a:
    :return:
    """
    b = []
    for i in a:
        c = []
        for j in str(i):
            c.append(str(i).count(j))
        if 2 in c:
            b.append(i)
    return b


if __name__ == '__main__':
    part1 = part1()
    print(len(part1))
    part2 = part2(part1)
    print(len(part2))
