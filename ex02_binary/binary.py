"""Converter."""


def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    digit = ""
    if dec == 0:
        digit = '0'
    else:
        while dec > 0:
            digit = str(dec % 2) + digit
            dec = dec // 2
    return digit


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    binary = list(binary)
    value = 0

    for i in range(len(binary)):
        digit = binary.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value


if __name__ == "__main__":
    print(dec_to_binary(145))  # -> 10010001
    print(dec_to_binary(245))  # -> 11110101
    print(dec_to_binary(255))  # -> 11111111

    print(binary_to_dec("1111"))  # -> 15
    print(binary_to_dec("10101"))  # -> 21
    print(binary_to_dec("10010"))  # -> 18
