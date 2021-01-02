"""Recursion is recursion."""


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    recursive_reverse("") => ""
    recursive_reverse("abc") => "cba"

    :param s: string
    :return: reverse of s
    """
    if not s:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def remove_nums_and_reverse(string):
    """
    Recursively remove all the numbers in the string and return reversed version of that string without numbers.

    print(remove_nums_and_reverse("poo"))  # "oop"
    print(remove_nums_and_reverse("3129047284"))  # empty string
    print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5oh565ty7p4"))  # "python for life"
    print(remove_nums_and_reverse("  k 4"))  # " k  "

    :param string: given string to change
    :return: reverse version of the original string, only missing numbers
    """
    if not string:
        return string
    elif string[0].isdigit():
        return remove_nums_and_reverse(string[1:])
    else:
        return remove_nums_and_reverse(string[1:]) + string[0]


def task1(string):
    """
    Figure out what this code is supposed to do and rewrite it using recursion.

    :param string: given string
    :return: figure it out
    """
    """for i in range(len(string)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True"""
    if len(string) == 1 or not string:
        return True
    while len(string) > 2:
        return task1(string[0] + string[2:])
    if string[0] == string[1]:
        return True
    else:
        return False


def task2(string):
    """
    Figure out what this code is supposed to do and rewrite it using iteration.

    :param string: given string
    :return: figure it out
    """
    """if len(string) < 2:
        return string
    elif string[0] == string[1]:
        return string[0] + "-" + task2(string[1:])
    return string[0] + task2(string[1:])"""
    if len(string) < 2:
        return string
    a = ""
    for i in range(len(string)):
        if i + 1 < len(string) and string[i + 1] == string[i]:
            a += string[i] + "-"
        else:
            a += string[i]
    return a


if __name__ == '__main__':
    # print(recursive_reverse("abc"))
    # print(remove_nums_and_reverse("poo"))  # "oop"
    # print(remove_nums_and_reverse("3129047284"))  # empty string
    # print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5oh565ty7p4"))  # "python for life"
    # print(remove_nums_and_reverse("  k 4"))  # " k  "
    print(task1("jeeeeeeeeeeje"))
